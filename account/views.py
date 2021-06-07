from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from . import forms

# Create your views here.

def sign_in(request):
    ctx = {'title': 'Sign In'}
    user = request.user
    redirect_to = request.GET.get('next')
    print(redirect_to)
    if user.is_authenticated:
        return redirect('home')
    if request.POST:        
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                return redirect('home')
    else:
        form = forms.SignInForm()
    ctx['form'] = form
    ctx['user'] = user
    return render(request, "account/sign_in.html", ctx)

def sign_up(request):
    ctx = {'title': 'Sign Up'}
    return render(request, "account/sign_up.html", ctx)

def sign_out(request):
    logout(request)
    return redirect('sign_in')