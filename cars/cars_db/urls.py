from django.urls import path
from . import views

urlpatterns = [
    #AppUsers
    path('appusers/', views.AppUserList.as_view()),
    path('appuser/<int:pk>/',views.AppUserDetail.as_view()),
    #CarModels
    path('carmodels/', views.CarModelList.as_view()),
    path('carmodel/<int:pk>/',views.CarModelDetail.as_view()),
    #Cars
    path('cars/', views.CarList.as_view()),
    path('car/<int:pk>/',views.CarDetail.as_view()),
    #Advertisements
    path('advertisements/', views.AdvertisementList.as_view()),
    path('advertisement/<int:pk>/',views.AdvertisementDetail.as_view()),
    #UserProfiles
    path('userprofiles/', views.UserProfileList.as_view()),
    path('userprofile/<int:pk>/',views.UserProfileDetail.as_view()),
]