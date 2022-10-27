from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Project, Task


def hello(request):
    return HttpResponse("<h1>Hola mundo</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")


def user(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)


def projects(request):
    project = list(Project.objects.values())
    return JsonResponse(project, safe=False)


def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse("task: %s" % task.title)
