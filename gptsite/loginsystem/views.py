from django.shortcuts import render
from django.http import HttpResponse

def loginindex(request):
    return HttpResponse("Loginpage")