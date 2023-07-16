from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# def landing_page(request):
# 	return redirect('index')


class LandingPageView(TemplateView):
	template_name = 'landing_page.html'


def testing_view(request):
	return HttpResponse('It works')
