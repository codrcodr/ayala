from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    ctx = {'title': 'Home Page'}
    return render(request, "core/index.html", ctx)