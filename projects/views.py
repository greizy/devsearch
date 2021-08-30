from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projectObjs = Project.objects.filter(status='active')
    context = {'projects' : projectObjs}
    return render(request, 'projects/projects.html',context)


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project' : projectObj}
    return render(request, 'projects/single-project.html',context)

def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, "projects/project_form.html",context)

# def confirmDeleteProject(request,pk):
#     projectObj = Project.objects.get(id=pk)
#     context = {"project" : projectObj}
#     return render(request, "projects/delete_template.html",context)

# def deleteProject(request,pk):
#     projectObj = Project.objects.get(id=pk)
#     projectObj.status = 'desactivated'
#     projectObj.save()
#     return redirect('projects')

def deleteProject(request,pk):
     projectObj = Project.objects.get(id=pk)
     context = {"project" : projectObj}
     if request.method == "POST":
        projectObj = Project.objects.get(id=pk)
        projectObj.status = 'desactivated'
        projectObj.save()
        return redirect('projects')         
     return render(request, "projects/delete_template.html",context)


def updateProject(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ProjectForm(instance=projectObj)
    if request.method == "POST":
        form = ProjectForm(request.POST,instance=projectObj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form' : form}
    return render(request, "projects/project_form.html",context)

