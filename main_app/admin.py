from django.contrib import admin
from .models import Petfinder_API_Token, Profile, Favorite


# Register your models here.

admin.site.register(Petfinder_API_Token)
admin.site.register(Profile)
admin.site.register(Favorite)