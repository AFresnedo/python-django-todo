from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Main routes
def index(request):
    todos = Todo.objects.all().order_by('text')
    users = User.objects.all()

    if request.method == "GET":
        # Display all the todos`
        return render(request, 'todoapp/index.html',
                { 'todos': todos, 'users': users })
    elif request.method == "POST":
        try:
            user_id = request.POST['userid']
        except:
            return render(request, 'todoapp/index.html',
                    { 'err': 'Please select your name',
                        'todos': todos,
                        'users': users })
        else:
            new_todo = Todo()
            new_todo.text = request.POST['text']
            new_todo.user = User.objects.get(pk=user_id)
            new_todo.save()
            return redirect('index')

def delete(request, todo_id):
    # Delete a todo
    Todo.objects.get(id=todo_id).delete()
    return redirect('index')

def done(request, todo_id):
    # mark a todo as complete
    item = Todo.objects.get(id=todo_id)
    item.is_complete = True
    item.save()
    return redirect('index')

# Auth-related routes
def signup(request):
    if request.method == 'GET':
        return render(request, 'todoapp/signup.html')
    elif request.method == 'POST':
        # NOTE these are the form names, request has the form data
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=username,
                    password=password)
            if user is not None:
                return login(request)
            else:
                return render(request,
                        'todoapp/signup.html', { 'err': 'Could not create' })
        except:
            return render(request, 'todoapp/signup.html',
            { 'err': 'Could not connect to DB' })

def login(request):
    if request.method == 'GET':
        return render(request, 'todoapp/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'todoapp/login.html',
                    { 'err': 'Failed to login' })

def logout(request):
    auth.logout(request)
    return redirect('index')
