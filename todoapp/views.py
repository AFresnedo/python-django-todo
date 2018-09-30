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
        return render(request, 'index.html',
                { 'todos': todos, 'users': users })

    elif request.method == "POST":
        try:
            user_id = request.POST['userid']
        except:
            return render(request, 'index.html',
                    { 'err': 'Please select your name',
                        'todos': todos,
                        'users': users, })
        else:
            new_todo = Todo()
            new_todo.text = request.POST['text']
            new_todo.user = User.objects.get(pk=user_id)
            new_todo.save()
            return redirect('index')

def delete(request, todo_id):

    # uses id= instead of pk=, just synonyms in this case
    Todo.objects.get(id=todo_id).delete()
    return redirect('index')

def done(request, todo_id):

    toMark = Todo.objects.get(pk=todo_id)
    toMark.is_complete = True
    toMark.save()
    return redirect('index')
