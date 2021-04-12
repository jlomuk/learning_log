from django.shortcuts import render
from django.http import HttpResponse

from .models import Topic, Entry


def get_homepage(request):
	"""Рендерит домашнюю страницу"""
	return render(request, 'learning_logs/index.html')


def get_topics(request):
	"""Выводит список тем отсортированную по дате добавления"""
	topics = Topic.objects.order_by('data_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


def get_topic_detail(request, pk):
	"""Получение записей по конретной теме"""
	topic = Topic.objects.get(pk=pk)
	entries = topic.entry_set.order_by('-data_added')
	context = {
		'topic': topic,
		'entries': entries,
	}
	return render(request,'learning_logs/topic_detail.html', context)