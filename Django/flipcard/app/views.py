from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Student


def home(resquest):
   
   # data={
   #  'name':'sanju',
   #  'age':'37',
   #  'active':True,
   #  'other':None
   # }
   # return JsonResponse(data)
    # return HttpResponse('<h1 style="background-color:green;">HELLO SANJU</h1>')
    # name="sanju"
    return render(resquest,'index.html')
    
    # return redirect("http://www.google.com/")#call any url
   
# def data(resquest):
#    return HttpResponse('<h1 style="background-color:green;">HELLO SANJU</h1>')
def data(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)
    name=request.POST.get("username")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    age=request.POST.get("age")
    volume=request.POST.get("volume")
    subscribe=request.POST.getlist("subscribe")
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
    print(resume)
    print(profilepic)
    # user_data={
    #     "name":name,
    #     "email":email,
    #     "phone":phone,
    #     "age":age,
    #     "volume":volume,
    #     "subscribe":subscribe,
    #     "gender":gender,
    #     "profilepic":profilepic,
    #     "resume":resume

    # }
    # print(user_data)
    # name="sanju",
    # email="sanju@gmail.com"
    Student.objects.create(name=name,email=email,phone=phone,age=age,volume=volume,subscribe=subscribe,gender=gender,profilepic=profilepic,resume=resume,)
    


