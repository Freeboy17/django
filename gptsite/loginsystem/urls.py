from django.urls import path

from .views import *

urlpatterns = [
    path('', loginindex),
    path('login/', login),
    path('register/', register)
]