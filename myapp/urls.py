from django.urls import path

from .views import *


urlpatterns = [
    path('', hello),
    path('about/', about),
    path('user/<str:username>', user),
    path('projects/', projects),
    path('tasks/<int:id>', tasks),
]
