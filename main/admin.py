from django.contrib import admin

# Register your models here.
from .models import Formation 
from .models import Category 

admin.site.register(Formation) 
admin.site.register(Category)