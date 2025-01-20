from django.contrib import admin
from .models import UserProfile,StudentData,AdminPage

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(StudentData)
admin.site.register(AdminPage)
