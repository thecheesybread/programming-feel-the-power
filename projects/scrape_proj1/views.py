# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
import proj1

def home(request):
    c = {'text':proj1.identity("you have come to project 1 home")}
    return render_to_response('proj1.html', c)




    
