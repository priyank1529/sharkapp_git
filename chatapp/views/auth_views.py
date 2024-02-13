from django.shortcuts import render
from chatapp.forms import CustomUserCreationForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from chatapp.models import CustomUser
import requests
import json
from django.http.response import JsonResponse
class CustomLoginView(LoginView):
    template_name='chatbox/index.html'
    
