from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Status
from django.views import View

def projects(request):
    ctx = {'title': 'Projects'}
    return render(request, "tracker/projects.html", ctx)

@login_required(login_url="sign_in")
def add_status(request):
    ctx = {'title':'Add Status'}
    if request.POST:
        status_form = forms.StatusForm(request.POST)
        if status_form.is_valid:
            status_form.save()
            return redirect('home')
    else:
        status_form = forms.StatusForm()
        ctx['form'] = status_form
    return render(request, 'tracker/add_status.html', ctx)

@login_required(login_url="sign_in")
def list_status(request):
    ctx = {'title':'List Status'}
    status_list = Status.objects.all()
    print(status_list)
    ctx['entries'] = status_list
    return render(request, 'tracker/list_status.html', ctx)
