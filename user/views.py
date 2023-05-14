from django.shortcuts import render,redirect
from . import models,forms
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthorized_user, admin_only
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required, user_passes_test

def error_404_view(request, exception):
    return render(request, '404.html')


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


# Create your views here.
@unauthorized_user
def afterlogin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')    
        else:
            error = 'Tài khoản hoặc mật khẩu không đúng'
            return render(request,'login.html' ,{'error':error})
    return render(request,'login.html')

@unauthorized_user
def signup_view(request):
    form1 = forms.StudentSignUpForm()
    form2 = forms.StudentForm()
    if request.method == 'POST':
        form1 = forms.StudentSignUpForm(request.POST)
        form2 = forms.StudentForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            #check if user exist  
            user = form1.save()
            user.set_password(user.password)
            user.save()
            form2.instance.user = user
            form2.save()
            group = Group.objects.get_or_create(name='STUDENT')
            group[0].user_set.add(user)
            return redirect('login')
        else:
            error = 'Tài khoản đã tồn tại'
            return render(request,'signup.html',{'form1':form1,'form2':form2,'error':error})
    return render(request,'signup.html',{'form1':form1,'form2':form2})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
# @admin_only
def home(request):
    group = None
    if request.user.groups.exists():
        group=request.user.groups.all()[0].name
        if group=='STUDENT':
            return redirect('student')
        if group=='TEACHER':
            return redirect('teacher')
        if group=='ADMIN':
            return redirect('admin-home')
    return redirect('logout')

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view(request):
    #count all model khoa
    khoa = models.Khoa.objects.all().count()
    #count all model lop
    lop = models.Lop.objects.all().count()
    #count all model monhoc
    monhoc = models.MonHoc.objects.all().count()
    #count all model giao vien
    giaovien = models.GiaoVien.objects.all().count()
    #count all model sinh vien
    sinhvien = models.SinhVien.objects.all().count()
    labels = ['Khoa','Lớp','Môn học','Giáo viên','Sinh viên']
    data = [khoa,lop,monhoc,giaovien,sinhvien]
    return render(request,'adminHome.html',{'labels':labels,'data':data})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_khoa_view(request):
    khoa = models.Khoa.objects.all()
    return render(request,'adminKhoa.html',{'khoa':khoa})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_khoa_add_view(request):
    form = forms.KhoaForm()
    if request.method == 'POST':
        form = forms.KhoaForm(request.POST)
        #kiểm tra tên khoa đã tồn tại chưa
        if form.is_valid():
            if models.Khoa.objects.filter(ten_khoa=request.POST['ten_khoa']).exists():
                error = 'Tên khoa đã tồn tại'
                return render(request,'adminKhoaThem.html',{'form':form,'error':error})  
            form.save()
            return redirect('admin-khoa')
    return render(request,'adminKhoaThem.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_khoa_update_view(request,pk):
    khoa = models.Khoa.objects.get(id=pk)
    form = forms.KhoaForm(instance=khoa)
    if request.method == 'POST':
        form = forms.KhoaForm(request.POST,instance=khoa)
        if form.is_valid():
            if models.Khoa.objects.filter(ten_khoa=request.POST['ten_khoa']).exists():
                error = 'Tên khoa đã tồn tại'
                return render(request,'adminKhoaThem.html',{'form':form,'error':error})
            form.save()
            return redirect('admin-khoa')
    return render(request,'adminKhoaThem.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_khoa_delete_view(request,pk):
    khoa = models.Khoa.objects.get(id=pk)
    khoa.delete()
    return redirect('admin-khoa')

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_lop_view(request):
    lop = models.Lop.objects.all()
    return render(request,'adminLop.html',{'lop':lop})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_lop_add_view(request):
    form = forms.LopForm()
    if request.method == 'POST':
        form = forms.LopForm(request.POST)
        if form.is_valid():
            if models.Lop.objects.filter(ten_lop=request.POST['ten_lop']).exists():
                error = 'Tên lớp đã tồn tại'
                return render(request,'adminLopThem.html',{'form':form,'error':error})  
            form.save()
            return redirect('admin-lop')
    return render(request,'adminLopThem.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_lop_update_view(request,pk):
    lop = models.Lop.objects.get(id=pk)
    form = forms.LopForm(instance=lop)
    if request.method == 'POST':
        form = forms.LopForm(request.POST,instance=lop)
        if form.is_valid():
            if models.Lop.objects.filter(ten_lop=request.POST['ten_lop']).exists():
                error = 'Tên lớp đã tồn tại'
                return render(request,'adminLopThem.html',{'form':form,'error':error})
            form.save()
            return redirect('admin-lop')
    return render(request,'adminLopThem.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_lop_delete_view(request,pk):
    lop = models.Lop.objects.get(id=pk)
    lop.delete()
    return redirect('admin-lop')

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_teacher_view(request):
    teacher = models.GiaoVien.objects.all()
    return render(request,'adminTeacher.html',{'teacher':teacher})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_teacher_add_view(request):
    form1 = forms.GiaoVienSignUpForm()
    form2 = forms.GiaoVienForm()
    if request.method == 'POST':
        form1 = forms.GiaoVienSignUpForm(request.POST)
        form2 = forms.GiaoVienForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            form2.instance.user = user
            form2.save()
            group = Group.objects.get_or_create(name='TEACHER')
            group[0].user_set.add(user)
            return redirect('admin-teacher')
        else:
            error = 'Tên đăng nhập đã tồn tại'
            return render(request,'adminTeacherThem.html',{'form1':form1,'form2':form2,'error':error})
    return render(request,'adminTeacherThem.html',{'form1':form1,'form2':form2})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_teacher_update_view(request,pk):
    teacher = models.GiaoVien.objects.get(id=pk)
    user = models.User.objects.get(id=teacher.user.id)
    form1 = forms.GiaoVienSignUpForm(instance=user)
    print(user.password)
    form2 = forms.GiaoVienForm(instance=teacher)
    if request.method == 'POST':
        form1 = forms.GiaoVienSignUpForm(request.POST,instance=user)
        form2 = forms.GiaoVienForm(request.POST,instance=teacher)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            form2.save()
            return redirect('admin-teacher')
        else:
            error = 'Tên đăng nhập đã tồn tại'
            return render(request,'adminTeacherThem.html',{'form1':form1,'form2':form2,'error':error})
    return render(request,'adminTeacherThem.html',{'form1':form1,'form2':form2})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_teacher_delete_view(request,pk):
    teacher = models.GiaoVien.objects.get(id=pk)
    user = models.User.objects.get(id=teacher.user.id)
    teacher.delete()
    user.delete()
    return redirect('admin-teacher')

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_student_view(request):
    student = models.SinhVien.objects.all()
    return render(request,'adminStudent.html',{'student':student})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_subject_view(request):
    subject = models.MonHoc.objects.all()
    return render(request,'adminMonhoc.html',{'subject':subject})

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_score_view(request):
    score = models.Diem.objects.all()
    return render(request,'adminDiem.html',{'score':score})

@login_required(login_url='login')
@user_passes_test(is_student)
def student_view(request):
    student = models.SinhVien.objects.all().filter(user=request.user)
    diem = models.Diem.objects.all().filter(sinh_vien=student[0])
    diem_trung_binh = []
    
    return render(request,'studentHome.html', {'student':student[0], 'diem':diem, 'diem_trung_binh':diem_trung_binh})

@login_required(login_url='login')
@user_passes_test(is_student)
def student_score_view(request):
    student = models.SinhVien.objects.all().filter(user=request.user)
    diem = models.Diem.objects.all().filter(sinh_vien=student[0])
    
    return render(request,'studentScore.html', {'diem':diem})

@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_view(request):
    teacher = models.GiaoVien.objects.all().filter(user=request.user)

    return render(request,'teacherHome.html', {'teacher':teacher[0]})

@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_subject_view(request):
    teacher = models.GiaoVien.objects.all().filter(user=request.user)
    monhoc = models.MonHoc.objects.all().filter(giao_vien=teacher[0])
    
    return render(request,'teacherSubject.html', {'monhoc':monhoc})

@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_score_view(request,pk):
    print(pk)
    monhoc = models.MonHoc.objects.get(id=pk)
    diem = models.Diem.objects.all().filter(mon_hoc=monhoc)
    
    return render(request,'teacherScore.html', {'diem':diem})

@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_update_view(request,pk):
    diem = models.Diem.objects.get(id=pk)
    form = forms.DiemForm(instance=diem)    
    if request.method == 'POST':
        form = forms.DiemForm(request.POST,instance=diem)
        if form.is_valid():
            form.save()
            return redirect('teacher-score',diem.mon_hoc.id)
    return render(request,'teacherUpdate.html',{'form':form, 'diem':diem})