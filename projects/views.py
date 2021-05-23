from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from projects.models import Project

# Create your views here.
@csrf_exempt
def get_project(request, project_title):
    if request.method == 'GET':
        try:
            project = Project.objects.get(title=project_title)
            response = json.dumps([{
                'title': project.title,
                'abstract': project.abstract,
                'description': project.description,
                'code': project.code,
                'deployment': project.deployment
            }])
        except:
            response = json.dumps([{
                'Error': 'No project found'
            }])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_all_projects(request):
    if request.method == 'GET':
        response_list = []
        projects = Project.objects.all()
        for project in projects:
            project_entry = {
                'title': project.title,
                'abstract': project.abstract,
                'description': project.description,
                'code': project.code,
                'deployment': project.deployment
            }
            response_list.append(project_entry)
        response_list.reverse()
        response = json.dumps(response_list)
        return HttpResponse(response, content_type='text/json')
    
    elif request.method == 'POST':
        return add_project(request)

@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        payload.reverse()
        
        try:
            for item in payload:
                title = item['title']
                abstract = item['abstract']
                description = item['description']
                code = item['code']
                deployment = item['deployment']
                project = Project(title=title, abstract=abstract, description=description, code=code, deployment=deployment)
                project.save()

            response = json.dumps([{
                'Success': 'Success!'
            }])
        except:
            response = json.dumps([{
                'Error': 'Project could not be added!'
            }])
        return HttpResponse(response, content_type='text/json')
    
    elif request.method == 'GET':
        return get_all_projects(request)
