from rest_framework import serializers
from . import models




### ===== APP_USER Serializers =====#####
class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppUser
        fields=['account_id','first_name','last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super(AppUserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1

class AppUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppUser
        fields=['account_id','first_name','last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super(AppUserDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1
### ===== END APP_USER Serializers =====#####


### ===== Car_Model Serializers =====#####
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarModel
        fields=['car_model_id','make', 'model']
    
    def __init__(self, *args, **kwargs):
        super(CarModelSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1

class CarModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarModel
        fields=['car_model_id','make', 'model']
    
    def __init__(self, *args, **kwargs):
        super(CarModelDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1
### ===== END Car_Model Serializers =====#####


### ===== Car Serializers =====#####
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields=['car_mod_id','registration_number', 'mileage']
    
    def __init__(self, *args, **kwargs):
        super(CarSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields=['car_mod_id','registration_number', 'mileage','number_of_doors', 'car_id']
    
    def __init__(self, *args, **kwargs):
        super(CarDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1
### ===== END Car Serializers =====#####


### ===== Advertisement Serializers =====#####
class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advertisement
        fields=['advertisement_date','seller_account', 'car_identification']
    
    def __init__(self, *args, **kwargs):
        super(AdvertisementSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advertisement
        fields=['advertisement_id','advertisement_date','seller_account', 'car_identification']
    
    def __init__(self, *args, **kwargs):
        super(AdvertisementDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1
### ===== END Advertisement Serializers =====#####



### ===== UserProfile Serializers =====#####
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields=['profile_id','acc_id','zip_code','city']
    
    def __init__(self, *args, **kwargs):
        super(UserProfileSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields=['profile_id','acc_id','zip_code','city', 'street_name','street_number']
    
    def __init__(self, *args, **kwargs):
        super(UserProfileDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1
        ### ===== END UserProfile Serializers =====#####
