from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
# Create your views here.


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():

            form.save() # Zapisanie uzytkownika do bazy danych
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, your account is created!")
            return redirect('login')

    else:
        form = RegisterForm()
        
    return render (request,"users/register.html", {"form": form})


def custom_logout_view(request):
    logout(request)
    return redirect('logout_success')