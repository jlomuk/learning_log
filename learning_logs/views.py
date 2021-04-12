from django.shortcuts import render
from django.http import HttpResponse


def get_homepage(request):
	return HttpResponse('Hello')
