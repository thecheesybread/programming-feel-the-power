# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest

def home(request):
    return HttpResponse('You have come to project 1 home')
