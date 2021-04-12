from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
	"""Регистрация нового пользователя"""
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return redirect('homepage')
	form = UserCreationForm(request.POST or None)
	context = {'form': form}
	return render(request, 'registration/register.html', context)