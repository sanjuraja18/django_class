from django.shortcuts import render
from .models import SanjuData

def home(request):
    return render(request, 'index.html')

def data(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)

    name=request.POST.get("username")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    age=request.POST.get("age")
    volume=request.POST.get("volume")
    subscribe=request.POST.get("subscribe")
    gender=request.POST.get("gender")
    profilepic=request.FILES.get("profile-pic")
    resume=request.FILES.get("resume")
    print(name)
    print(email)
    print(phone)
    print(age)
    print(volume)
    print(subscribe)
    print(gender)
    print(profilepic)
    print(resume)

    SanjuData.objects.create(name=name,email=email,phone=phone,age=age,volume=volume,subscribe=subscribe,gender=gender,profilepic=profilepic,resume=resume)

    
