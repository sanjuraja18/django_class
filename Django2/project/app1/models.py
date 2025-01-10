from django.db import models

class SanjuData(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    age=models.IntegerField()
    volume=models.IntegerField()
    subscribe=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    profilepic=models.FileField(max_length=50)
    resume=models.FileField(max_length=50)
