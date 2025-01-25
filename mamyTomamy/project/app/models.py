from django.db import models

v_nm=[("tata","tata"),("hero","hero"),("bmw","bmw"),("audi","audi"),]
class vehicle(models.Model):
    veh_name=models.CharField(max_length=50,choices=v_nm)
    def __srt__(self):
        return self.veh_name


f_nm=[("petrol","petrol"),("cng","cng"),("dsl","dsl"),("ev","ev"),]
class fuel(models.Model):
    f_name=models.CharField(max_length=50,choices=f_nm)
    v_name=models.ManyToManyField(vehicle)
    def __srt__(self):
        return str(self.f_name)
    