from django.shortcuts import render

# Create your views here.
from .models import Student

def alldata(request):
    # x=Student.objects.all()
    # print(x)
    # y=Student.objects.filter(stu_name='sanju')
    # print(y)
    # x=Student.objects.filter(stu_name='sanju thakur')
    # print(x)

    # z=Student.objects.exclude(stu_name='sanju')
    # print(z)

    # q=Student.objects.order_by('stu_name')
    # print(q)

    # r=Student.objects.order_by('-stu_name')
    # print(r)

    # v=Student.objects.values()
    # print(v)
    #  m=Student.objects.get(stu_name='sanju')
    #print(m)
    #m=Student.objects.get(stu_email='sanju')
    # print(m)
    x=Student.objects.all()
    data={
        'data':x.values()
    }
    return render(request,'first.html',data)
    print(x)

def filter(request):
    data=Student.objects.filter(stu_email="sanju@gmail.com")
    print(data)

def velueData(request):
    data=Student.objects.values()
    print(data)

def veluesList(request):
    data=Student.objects.values_list()
    print(data)

def exclude(request):
    data=Student.objects.exclude(stu_name="sanju")
    print(data)

def get(request):
    data=Student.objects.get(stu_name="sanju raja")
    print(data)

def firstdata(request):
    data=Student.objects.first()
    print(data)

    print(data.id)
    print(data.stu_name)
    print(data.stu_email)
    print(data.stu_contact)

def lastdata(request):
    data=Student.objects.last()
    print(data)

def orderby(request):
    data=Student.objects.order_by('-id')[0:3]
    print(data)
    # data=Student.objects.all()[0:4]
    # print(data)





