from django.conf.urls import url
from . import views
from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import redirect, render

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

def login(request):
    return HttpResponse('login')

def logout(request):
    auth.logout(request)
    return redirect('index')
