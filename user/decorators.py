from django.http.response import HttpResponse
from django.shortcuts import render,redirect

def unauthorized_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                if group=='STUDENT':
                    return redirect('student')
                if group=='TEACHER':
                    return redirect('teacher')
                if group=='ADMIN':
                    return redirect('admin-home')
            return redirect('login')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            print(request.user)
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                print('Working')
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator
 
def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        print(request.user)
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='STUDENT':
            return redirect('student')
        if group=='TEACHER':
            return redirect('teacher')
        if group=='ADMIN':
            return redirect('admin-home')
        else:
            return redirect('/logout')
    return wrapper_function