from django.shortcuts import render

# Create your views here.


def sign_in(request):
    return render(request, 'login/login.html')


def sign_up(request):
    return render(request, 'login/sign_up.html')


def home(request):
    return render(request, 'home.html')


def create(request):
    return render(request, 'users/create.html')


def update(request):
    return render(request, 'users/update.html')


def user(request):
    return render(request, 'users/read.html')