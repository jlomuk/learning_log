from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


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


def add_new_topic(request):
	"""Создае новую тему для изучения"""
	if request.method == 'POST':
		form = TopicForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('topics')	
	form = TopicForm(request.POST or None)
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


def add_new_entry(request, pk):
	"""Добавляет новую запись к конкретной теме"""
	topic = Topic.objects.get(pk=pk)
	if request.method == 'POST':
		form = EntryForm(request.POST or None)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('topic_detail', pk=pk)
	form = EntryForm(request.POST or None)
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/add_new_entry.html', context)


def edit_entry(request, pk):
	"""Редактирует существующую запись"""
	entry = Entry.objects.get(pk=pk)
	topic = entry.topic
	print(topic)
	if request.method == 'POST':
		form = EntryForm(request.POST, instance=entry)
		if form.is_valid():
			form.save()
			return redirect('topic_detail', pk=topic.id)
	form = EntryForm(instance=entry)
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)

