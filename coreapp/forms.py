from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=140, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','name','email', 'password1', 'password2']