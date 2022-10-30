from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse


# Create your views here.
from .models import Project, Task
from .forms import Create_new_project, Create_new_task


def index(request):
    title = 'Welcome to Django'
    return render(request, 'index.html', {'title': title})


def about(request):
    username = "Juan"
    return render(request, 'about.html', {'username': username})


def user(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)


def project(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'project.html', {'project': project, 'tasks': tasks})


def projects(request):
    # project = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {'form': Create_new_project()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
                
                
def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': Create_new_task()})
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=3)
        return redirect('tasks')
                

