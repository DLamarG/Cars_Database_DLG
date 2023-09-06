from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Vendor Models
class AppUser(models.Model):
    account_id=models.AutoField(primary_key=True)
    first_name=models.TextField(max_length=50,blank=False)
    last_name=models.TextField(max_length=50,blank=False)
    email=models.EmailField(max_length=200,blank=True)
    password=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50,blank=True)
    model = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"{self.car_model_id}"
    
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_mod_id = models.ForeignKey(CarModel,on_delete=models.SET_NULL,null=True,related_name='car')
    number_of_owners = models.IntegerField()
    registration_number = models.CharField(max_length=30)
    manufacture_year = models.BigIntegerField()
    number_of_doors = models.IntegerField()
    mileage = models.BigIntegerField()

    def __str__(self):
        return f"{self.car_id} {self.car_mod_id} {self.mileage}"
    
class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    advertisement_date = models.DateField(auto_now=True)
    seller_account = models.ForeignKey(AppUser,on_delete=models.CASCADE, related_name='app')
    car_identification = models.ForeignKey(Car,on_delete=models.CASCADE, related_name='carid')

    def __str__(self):
        return f"{self.advertisement_id} {self.seller_account}"
    

class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    acc_id = models.ForeignKey(AppUser,on_delete=models.CASCADE, related_name='appU')
    street_name = models.CharField(max_length=100,blank=False)
    street_number = models.BigIntegerField()
    zip_code = models.BigIntegerField()
    city = models.CharField(max_length=50)