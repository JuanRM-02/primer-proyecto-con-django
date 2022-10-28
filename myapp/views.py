from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Project, Task


def index(request):
    title = 'Welcome to Django'
    return render(request, 'index.html', {'title': title})


def about(request):
    username = "Juan"
    return render(request, 'about.html', {'username': username})


def user(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)


def projects(request):
    # project = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})
