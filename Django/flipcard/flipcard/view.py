from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(resquest):
    x=10
    y=20
    return HttpResponse('<h1 style="background-color:red;">HELLO SANJU</h1>')