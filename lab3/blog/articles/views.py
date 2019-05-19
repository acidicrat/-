from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(u'Welcome to the site!', content_type="text/plain")


# Create your views here.
