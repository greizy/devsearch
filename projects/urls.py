
from django.urls import path
from django.http import HttpResponse
from .views import *


urlpatterns = [
    path('projects/',projects, name="projects"),
    path('project/<str:pk>/', project, name='project'),
]

