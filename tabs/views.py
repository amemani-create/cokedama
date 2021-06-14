from django.shortcuts import render
from django.http import HttpResponse


def main_home(request):
    return render(request, 'tabs/main_home.html')


def about_us(request):
    return render(request, 'tabs/about_us.html')


def recycle(request):
    return render(request, 'tabs/recycle.html')


def join_us(request):
    return render(request, 'tabs/join_us.html')

def consult(request):
    return render(request, 'tabs/consult.html')