from django.db import models

# Create your models here.
# phone=phone,age=age,volume=volume,subscribe=subscribe,gender=gender,profilepic=profilepic,resume=resume,)
    


class Student(models.Model):
    name=models.CharField(max_length=50)
    email= models.EmailField()
    phone=models.IntegerField()
    subscribe=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    profilepic=models.FileField(max_length=50)
    resume=models.FileField(max_length=50)
    volume=models.IntegerField()
    

