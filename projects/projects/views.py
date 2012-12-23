from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
def home(request):
    c = {'text':'you have come to main home'}
    return render_to_response('text.html', c)
