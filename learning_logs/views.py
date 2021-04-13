from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from . import utils


def get_homepage(request):
	"""Рендерит домашнюю страницу"""
	return render(request, 'learning_logs/index.html')


@login_required
def get_topics(request):
	"""Выводит список тем отсортированную по дате добавления"""
	topics = Topic.objects.filter(owner=request.user).order_by('data_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


@login_required
def get_topic_detail(request, pk):
	"""Получение записей по конретной теме"""
	topic = Topic.objects.get(pk=pk)
	utils.check_topic_owner(request, topic)
	entries = topic.entry_set.order_by('-data_added')
	context = {
		'topic': topic,
		'entries': entries,
	}
	return render(request,'learning_logs/topic_detail.html', context)


@login_required
def add_new_topic(request):
	"""Создае новую тему для изучения"""
	if request.method == 'POST':
		form = TopicForm(request.POST or None)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('topics')	
	form = TopicForm(request.POST or None)
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


@login_required
def add_new_entry(request, pk):
	"""Добавляет новую запись к конкретной теме"""
	topic = Topic.objects.get(pk=pk)
	utils.check_topic_owner(request, topic)
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


@login_required
def edit_entry(request, pk):
	"""Редактирует существующую запись"""
	entry = Entry.objects.get(pk=pk)
	topic = entry.topic
	utils.check_topic_owner(request, topic)
	if request.method == 'POST':
		form = EntryForm(request.POST, instance=entry)
		if form.is_valid():
			form.save()
			return redirect('topic_detail', pk=topic.id)
	form = EntryForm(instance=entry)
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)

