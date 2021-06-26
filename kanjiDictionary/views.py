from django.shortcuts import render
from django.http import HttpResponse
from .models import userInformations

# Create your views here.

def index(request):
    return render(request,'kanjiDictionary/index.html')

def checkLogin(request, id, password):
    if request.method == 'POST' :
        userModel = userInformations(request.POST)
    # login failed
    
    # login success
    return render(request,'')
    