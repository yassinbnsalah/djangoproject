from django.forms import ModelForm
from .models import Category, Formation 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class FormationForm(ModelForm):
    class Meta:
        model = Formation 
        fields = '__all__' 

class CategoryForm(ModelForm):
    class Meta:
        model = Category 
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','password1' ,'password2'] 
        