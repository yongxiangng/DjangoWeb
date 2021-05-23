from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from about.models import About

# Create your views here.
@csrf_exempt
def get_about(request):
    if request.method == 'GET':
        response_list = []
        about_list = About.objects.all()
        for item in about_list:
            about_entry = {
                'text': item.text
            }
            response_list.append(about_entry)
        response_list.reverse()
        response = json.dumps(response_list)
        return HttpResponse(response, content_type='text/json')
    
    elif request.method == 'POST':
        return add_about(request)

@csrf_exempt
def add_about(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        payload.reverse()
        print(payload)
        try:
            for item in payload:
                text = item['text']
                about = About(text=text)
                about.save()

            response = json.dumps([{
                'Success': 'Success!'
            }])
        except:
            response = json.dumps([{
                'Error': 'Award could not be added!'
            }])
        return HttpResponse(response, content_type='text/json')
    
    elif request.method == 'GET':
        return get_about(request)
