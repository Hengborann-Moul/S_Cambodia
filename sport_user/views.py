from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as auth_login

# Create your views here.
from sport_user.form import UserForm, PlaygroundForm
from sport_user.models import Playground


def index(request):
    return HttpResponse("<h1> Welcome to Sport Cambodia</h1>")


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        return render(request, 'sport_user/login.html')

    context = {
        "form": form,
    }
    return render(request, 'sport_user/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                playground = Playground.objects.filter(user=request.user)

                return render(request, 'sport_user/create_playground.html', {'playground': playground})
            else:
                return render(request, 'sport_user/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'sport_user/login.html', {'error_message': 'Indvaile'})
    return render(request, 'sport_user/login.html')


def playground(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>Come Again</h1>")
    else:
        form = PlaygroundForm(request.POST)

        if form.is_valid():
            playground = form.save(commit=False)
            playground.user = request.user
            playground.save()
            return HttpResponse("<h1>Good Job </h1>")
        commit = {
            'form': form
        }
    return render(request, 'sport_user/playground.html')


def user_logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'sport_user/login.html', context)
