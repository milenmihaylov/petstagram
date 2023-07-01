from django.http import HttpResponse
from django.shortcuts import render, redirect


def landing_page(request):
    return redirect('index')


def testing_view(request):
    return HttpResponse('It works')
