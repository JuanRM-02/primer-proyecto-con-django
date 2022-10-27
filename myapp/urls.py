from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('about/', about),
    path('user/', user),
    path('projects/', projects),
    path('tasks/', tasks),
]
