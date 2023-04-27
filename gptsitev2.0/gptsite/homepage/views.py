from django.shortcuts import render
#from django.http import HttpResponse
from . import forms
from django.contrib.auth import login, authenticate, logout  # add to imports
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 


def home(request):
    return render(request, 'homepage/home.html')
# def login(request):
#     return render(request, 'homepage/login.html')
# def register(request):
#     return render(request, 'homepage/register.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(home)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="homepage/login.html", context={"login_form":form})

def logout_user(request):
    logout(request)
    return redirect('login')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(login)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="homepage/register.html", context={"register_form":form})