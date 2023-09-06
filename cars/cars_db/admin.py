from django.contrib import admin
from . import models

admin.site.register(models.AppUser)
admin.site.register(models.UserProfile)
admin.site.register(models.Advertisement)
admin.site.register(models.Car)
admin.site.register(models.CarModel)