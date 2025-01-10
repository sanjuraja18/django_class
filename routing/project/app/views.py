from django.shortcuts import render

def Landingpage(request):
    return render(request,'home.html')