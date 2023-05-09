from django.contrib import admin
from .models import Khoa
from .models import GiaoVien
from .models import MonHoc
from .models import Lop
from .models import SinhVien
from .models import Diem

# Register your models here.
admin.site.register(Khoa)
admin.site.register(GiaoVien)
admin.site.register(MonHoc)
admin.site.register(Lop)
admin.site.register(SinhVien)
admin.site.register(Diem)

