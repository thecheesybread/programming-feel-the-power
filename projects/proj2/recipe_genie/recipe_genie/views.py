from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)
