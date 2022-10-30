from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('user/', user, name='user'),
    path('projects/', projects, name='projects'),
    path('create_project/', create_project, name='create_project'),
    path('tasks/', tasks, name='tasks'),
    path('create_task/', create_task, name='create_task'),
]
