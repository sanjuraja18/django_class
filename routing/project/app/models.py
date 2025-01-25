from django.db import models

# Create your models here.
class UserProfile(models.Model):
    adharno=models.IntegerField(unique=True)
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,null=True,unique=True,db_index=True,blank=False,help_text="Enter a unique username")
    email=models.EmailField(max_length=255,unique=True,blank=False,db_index=True)
    bio=models.CharField(max_length=50,blank=True,null=True,db_index=True,help_text="Write a short bio about yourself")
    is_active=models.BooleanField(default=False,db_index=True)
    quail=[('b-tech','b-tech'),('m,tech','m-tech')]
    qulification=models.CharField(max_length=100,choices=quail,null=True,verbose_name='Quali',db_index=True)
    

    
class StudentData(models.Model):
    sno=models.AutoField(primary_key=True)
    adharno=models.OneToOneField(UserProfile,on_delete=models.PROTECT,)
    username=models.CharField(max_length=30,null=True,unique=True,db_index=True,blank=False,help_text="Enter a unique username")
    email=models.EmailField(max_length=255,unique=True,blank=False,db_index=True)
    bio=models.CharField(max_length=50,blank=True,null=True,db_index=True,help_text="Write a short bio about yourself")
    is_active=models.BooleanField(default=False,db_index=True)
    quail=[('b-tech','b-tech'),('m,tech','m-tech')]
    qulification=models.CharField(max_length=100,choices=quail,null=True,verbose_name='Quali',db_index=True)
    def __str__(self):
        return str(self.adharno)

       


class AdminPage(models.Model):
    sno=models.AutoField(primary_key=True)
    adminname=models.CharField(max_length=30,null=True,unique=True,db_index=True,blank=False,help_text="Enter a unique username")
    email=models.EmailField(max_length=255,unique=True,blank=False,db_index=True)
    bio=models.CharField(max_length=50,blank=True,null=True,db_index=True,help_text="Write a short bio about yourself")
    is_active=models.BooleanField(default=False,db_index=True)



    
department=[("CSE","CSE"),("EXE","EXE"),("IT","IT"),("ME","ME"),("MI/MI","MI/MI")]
class DepartmentModel(models.Model):
    dep_name=models.CharField(max_length=100,verbose_name="name", choices=department, unique=True)
    description=models.TextField(max_length=200,verbose_name="Desc")
    def __str__(self):
        return str(self.dep_name)

Cources=[("1","B.Tech"),("2","B.Com"),("3","M.Com"),("4","BCA"),("5","M.Tech")]
class Student(models.Model):
    name=models.CharField(max_length=100,verbose_name="name", choices=Cources)
    age=models.IntegerField()
    email=models.EmailField()
    stu_name=models.ForeignKey(DepartmentModel,on_delete=models.PROTECT, to_field='dep_name')
    def __str__(self):
        return str(self.stu_name)

fueltype=[("petool","petool"),("EV","EV"),("CNG","CNG"),("Dezal","Dezal")]
class fuel(models.Model):
    fuel_name=models.CharField(max_length=100,verbose_name="name", choices=fueltype,primary_key=True)
    def __str__(self):
        return str(self.fuel_name)

vehicalType=[("TATA","TATA"),("HONDA","HONDA"),("MARUTHI","MARUTHI"),("BMW","BMW")]
class Vehical(models.Model):
    car_name=models.CharField(max_length=100,verbose_name="name", choices=vehicalType, primary_key=True)
    price=models.IntegerField()
    fuel_name=models.ManyToManyField(fuel)
    def __str__(self):
        return self.car_name