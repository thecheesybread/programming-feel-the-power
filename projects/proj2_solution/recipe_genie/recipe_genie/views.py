from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.utils import simplejson as json
from django.http import HttpResponse
import genie

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def get_recipes(request):
    ingredients = json.loads(request.GET['ingredients'])
    if ingredients == []:
        return HttpResponse('[]')
    result_recipes = genie.find_recipes(ingredients)
    return HttpResponse(json.dumps(result_recipes))

