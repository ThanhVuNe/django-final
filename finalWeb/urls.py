"""finalWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('admin-home', views.admin_view,name='admin-home'),
    path('admin-khoa', views.admin_khoa_view,name='admin-khoa'),
    path('admin-khoa-add', views.admin_khoa_add_view,name='admin-khoa-add'),
    path('admin-khoa-update/<int:pk>', views.admin_khoa_update_view,name='admin-khoa-update'),
    path('admin-khoa-delete/<int:pk>', views.admin_khoa_delete_view,name='admin-khoa-delete'),
    path('admin-lop', views.admin_lop_view,name='admin-lop'),
    path('admin-lop-add', views.admin_lop_add_view,name='admin-lop-add'),
    path('admin-lop-update/<int:pk>', views.admin_lop_update_view,name='admin-lop-update'),
    path('admin-lop-delete/<int:pk>', views.admin_lop_delete_view,name='admin-lop-delete'),
    path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
    path('admin-teacher-add', views.admin_teacher_add_view,name='admin-teacher-add'),
    path('admin-teacher-update/<int:pk>', views.admin_teacher_update_view,name='admin-teacher-update'),
    path('admin-teacher-delete/<int:pk>', views.admin_teacher_delete_view,name='admin-teacher-delete'),
    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-monhoc', views.admin_subject_view,name='admin-monhoc'),
    path('admin-diem', views.admin_score_view,name='admin-diem'),

    path('student', views.student_view,name='student'),
    path('student-score', views.student_score_view,name='student-score'),

    path('teacher', views.teacher_view,name='teacher'),
    path('teacher-subject', views.teacher_subject_view,name='teacher-subject'),
    path('teacher-score/<int:pk>', views.teacher_score_view,name='teacher-score'),
    path('teacher-update/<int:pk>', views.teacher_update_view,name='teacher-update'),
    path('logout', views.logout_view,name='logout'),

    path('signup', views.signup_view,name='signup'),
    path('login', views.afterlogin_view,name='login'),
]

handle404 = 'user.views.error_404_view'