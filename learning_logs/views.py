from django.shortcuts import render
from django.http import HttpResponse


def get_homepage(request):
	return render(request, 'learning_logs/index.html')
