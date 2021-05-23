from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from awards.models import Award

# Create your views here.
@csrf_exempt
def get_award(request, award_title):
    if request.method == 'GET':
        try:
            award = Award.objects.get(title=award_title)
            response = json.dumps([{
                'date': award.date,
                'title': award.title,
                'description': award.description
            }])
        except:
            response = json.dumps([{
                'Error': 'No award found'
            }])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_all_awards(request):
    if request.method == 'GET':
        response_list = []
        awards = Award.objects.all()
        for award in awards:
            award_entry = {
                'date': award.date,
                'title': award.title,
                'description': award.description
            }
            response_list.append(award_entry)
        response_list.reverse()
        response = json.dumps(response_list)
        return HttpResponse(response, content_type='text/json')
    
    elif request.method == 'POST':
        return add_award(request)

@csrf_exempt
def add_award(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        payload.reverse()
        
        try:
            for item in payload:
                date = item['date']
                title = item['title']
                description = item['description']
                award = Award(date=date, title=title, description=description)
                award.save()

            response = json.dumps([{
                'Success': 'Success!'
            }])
        except:
            response = json.dumps([{
                'Error': 'Award could not be added!'
            }])
        return HttpResponse(response, content_type='text/json')
    
    elif request.method == 'GET':
        return get_all_awards(request)
