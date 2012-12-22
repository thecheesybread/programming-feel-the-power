from django.http import HttpResponse, HttpResponseBadRequest

def home(request):
    return HttpResponse('You have come to main home')
