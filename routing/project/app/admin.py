from django.contrib import admin
from .models import UserProfile,StudentData,AdminPage,DepartmentModel,Student

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(StudentData)
admin.site.register(AdminPage)
admin.site.register(DepartmentModel)
admin.site.register(Student)
