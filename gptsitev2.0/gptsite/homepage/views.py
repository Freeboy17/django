from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    return render(request, 'homepage/home.html')
def login(request):
    return render(request, 'homepage/login.html')
def register(request):
    return render(request, 'homepage/register.html')