from django.contrib import admin
from .models import UserProfile,StudentData,AdminPage,DepartmentModel,Student,fuel,Vehical

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(StudentData)
admin.site.register(AdminPage)
admin.site.register(DepartmentModel)
admin.site.register(Student)
admin.site.register(fuel)
admin.site.register(Vehical)
