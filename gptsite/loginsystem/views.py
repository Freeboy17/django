from django.shortcuts import render
from django.http import HttpResponse

def loginindex(request):
    return HttpResponse("Loginpage")

def login(request):
    return render(request, 'loginsystem/login_page.html')
def register(request):
    return render(request, 'loginsystem/register_page.html')