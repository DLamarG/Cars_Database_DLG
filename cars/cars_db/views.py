from . import serializers
from rest_framework import generics
from . import models


####----- App-User Views -----####
class AppUserList(generics.ListCreateAPIView):
    queryset=models.AppUser.objects.all()
    serializer_class=serializers.AppUserSerializer


class AppUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.AppUser.objects.all()
    serializer_class=serializers.AppUserDetailSerializer
####----- END App-User Views -----####



####----- Car_Model Views -----####
class CarModelList(generics.ListCreateAPIView):
    queryset=models.CarModel.objects.all()
    serializer_class=serializers.CarModelSerializer

class CarModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.CarModel.objects.all()
    serializer_class=serializers.CarModelSerializer
####----- END Car_Model Views -----####



####----- Car Views -----####
class CarList(generics.ListCreateAPIView):
    queryset=models.Car.objects.all()
    serializer_class=serializers.CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Car.objects.all()
    serializer_class=serializers.CarDetailSerializer
####----- END Car Views -----####



####----- Advertisement Views -----####
class AdvertisementList(generics.ListCreateAPIView):
    queryset=models.Advertisement.objects.all()
    serializer_class=serializers.AdvertisementSerializer

class AdvertisementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Advertisement.objects.all()
    serializer_class=serializers.AdvertisementDetailSerializer
####----- END Advertisement Views -----####



####----- User_Profile Views -----####
class UserProfileList(generics.ListCreateAPIView):
    queryset=models.UserProfile.objects.all()
    serializer_class=serializers.UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.UserProfile.objects.all()
    serializer_class=serializers.UserProfileDetailSerializer
####----- END User_Profile Views -----####
