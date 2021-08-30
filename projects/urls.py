
from django.urls import path
from django.http import HttpResponse
from .views import *


urlpatterns = [
    path('', projects, name="projects"),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', createProject, name = 'createProject'),
    path('delete-project/<str:pk>/', deleteProject, name = 'deleteProject'),
    #path('confirm-delete-project/<str:pk>/', confirmDeleteProject, name = 'confirmDeleteProject'),
    path('update-project/<str:pk>/', updateProject, name = 'updateProject'),
]

