from django.http import HttpResponse
from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing_page.html')


def testing_view(request):
    return HttpResponse('It works')

def add_comment(request, pk):
    pass
