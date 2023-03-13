from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from  .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    data = {
        'form':UserRegisterForm()
    }
    if request.method == 'POST':
        form_reg = UserRegisterForm(request.POST)
        if form_reg.is_valid():
            form_reg.save()
            username = form_reg.cleaned_data["username"]
            password = form_reg.cleaned_data["password1"]
            password_confirm = form_reg.cleaned_data["password2"]
            
            if password == password_confirm:
                user = authenticate(username=username, password=password)
                login(request, user)
            
                #redirect to home
                return redirect(to='index')
            else:
                messages.error("Passwords doesn't match")
        
    return render(request, 'registration/register.html', data)

def media(request):
    pass

