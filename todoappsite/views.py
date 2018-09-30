from django.conf.urls import url
from . import views
from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import redirect, render
# alternatively, can just type auth.models.User every time
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html')

    elif request.method == 'POST':
        print('hello justin', request.POST['username'])
        print('this should look familiar', request.POST['password'])
        # set attributes AND save
        newUser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'])
        return redirect('index')

def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('username attempting to login:', username)
        print('with password:', password)
        # uses Django's built in authentication
        user = authenticate(request, username=username, password=password)
        # if a user object was returned, it passed the check
        if user is not None:
            # pass the request (why?) and the authenticated user
            #   NOTE that any data set during the anonymous session is retained in
            #   the session after a user logs in.
            # ^ may be why, don't want to lose non-user-obj data that was in req
            # NOTE that sessions are inside of the request object
            auth.login(request, user)
            return redirect('index')
        # if authenticate method did not return a user, it failed the check
        else:
            return render(request, 'auth/login.html',
                    { 'err': 'That is not a valid login' })


def logout(request):
    # NOTE sending it request to clear out request.sessions or other relevants
    auth.logout(request)
    return redirect('index')
