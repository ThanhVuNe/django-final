from django import forms
from . import models
from django.contrib.auth.models import User

class StudentSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','password']

class StudentForm(forms.ModelForm):
    ngay_sinh = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'))
    gioi_tinh = forms.ChoiceField(choices=[('Nam','Nam'),('Nữ','Nữ')])
    class Meta:
        model = models.SinhVien
        fields = ['ten_sinh_vien','gioi_tinh','ngay_sinh','lop']

class DiemForm(forms.ModelForm):
    #set min and max value for diem_chuyen_can
    diem_chuyen_can = forms.FloatField(min_value=0,max_value=10)
    diem_giua_ki = forms.FloatField(min_value=0,max_value=10)
    diem_cuoi_ki = forms.FloatField(min_value=0,max_value=10)
    class Meta:
        model = models.Diem
        fields = ['diem_chuyen_can','diem_giua_ki','diem_cuoi_ki']
        
class KhoaForm(forms.ModelForm):
    class Meta:
        model = models.Khoa
        fields = ['ten_khoa','so_dien_thoai']

class LopForm(forms.ModelForm):
    class Meta:
        model = models.Lop
        fields = ['ten_lop','khoa']

class GiaoVienForm(forms.ModelForm):
    ngay_sinh = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'))
    class Meta:
        model = models.GiaoVien
        fields = ['ten_giao_vien','ngay_sinh','khoa']

class GiaoVienSignUpForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(), )
    class Meta:
        model = User
        fields = ['username','password']