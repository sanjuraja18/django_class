from django.contrib import admin

# Register your models here.
from .models import vehicle,fuel

admin.site.register(vehicle)
admin.site.register(fuel)
