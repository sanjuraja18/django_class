
# from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="index"),
    path('data/', views.data, name='data')
]
