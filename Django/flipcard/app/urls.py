
# from django.contrib import admin
from django.urls import path
# from .view import home
# from .import view
from app import views

urlpatterns = [
    # path('', home)
    path('', views.home, name='index'),
    path('data/', views.data, name='data')
    

]
