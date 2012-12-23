# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.utils import simplejson as json
import proj1

def home(request):
    c = {'text':proj1.identity("you have come to project 1 home <br> ")}
    return render_to_response('proj1.html', c)


def get_craigslist_info(request):
    json_data = json.loads(request.raw_post_data)
    craigslist_url = json_data['craigslist_url'].strip()
    try:
        return HttpResponse(json.dumps(proj1.get_craigslist_info(craigslist_url)))
    except:
        return HttpResponse("ERROR")

    
