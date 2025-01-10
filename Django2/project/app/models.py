from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    age=models.IntegerField(max_length=50)
    subscribe=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    profilepic=models.FileField(max_length=50)
    resume=models.FileField(max_length=50)
    volume=models.IntegerField()