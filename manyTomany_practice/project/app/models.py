from django.db import models

# Create your models here.
v_nm=[("Tata","Tata"),("BMW","BMW"),("HERO","HERO"),("AUDI","AUDI")]
class vehicle(models.Model):
    veh_name=models.CharField(max_length=50, choices=v_nm)
    def __str__(self):
        return self.veh_name


f_nm=[("petrol","petrol"),("cng","cng"),("dsl","dsl"),("ev","ev")]
class fuel(models.Model):
    f_name=models.CharField(max_length=50, choices=f_nm)
    v_nm=models.ManyToManyField(vehicle)
    def __str__(self):
        return self.f_name
