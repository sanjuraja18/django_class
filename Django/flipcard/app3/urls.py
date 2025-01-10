from django.contrib import admin
from django.urls import path
# from .view import home
# from .import view
from app3 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home)
    path('', views.home)
]
