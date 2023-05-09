from django.db import models

# Create your models here.
class Khoa(models.Model):
    ten_khoa = models.CharField(max_length=100)
    so_dien_thoai = models.CharField(max_length=15)
    def __str__(self):
        return self.ten_khoa

class GiaoVien(models.Model):
    ten_giao_vien = models.CharField(max_length=100)
    ngay_sinh = models.DateField()
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten_giao_vien

class MonHoc(models.Model):
    ten_mon_hoc = models.CharField(max_length=100)
    so_tin_chi = models.IntegerField()
    giao_vien = models.ForeignKey(GiaoVien, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten_mon_hoc

class Lop(models.Model):
    ten_lop = models.CharField(max_length=100)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten_lop

class SinhVien(models.Model):
    ten_sinh_vien = models.CharField(max_length=100)
    gioi_tinh = models.CharField(max_length=10)
    ngay_sinh = models.DateField()
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten_sinh_vien

class Diem(models.Model):
    mon_hoc = models.ForeignKey(MonHoc, on_delete=models.CASCADE)
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    diem_chuyen_can = models.FloatField()
    diem_giua_ki = models.FloatField()
    diem_cuoi_ki = models.FloatField()
    def __str__(selft):
        return selft.mon_hoc.ten_mon_hoc + " - " + selft.sinh_vien.ten_sinh_vien