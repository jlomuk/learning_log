from django import forms

from . import models


class TopicForm(forms.ModelForm):
	"""Форма для создания новый тем для изучения"""
	class Meta:
		model = models.Topic
		fields = ['text']
		labels= {'text':'Введите тему для добавления'}


class EntryForm(forms.ModelForm):
	"""Форма для создания новых записей в темах для изучения"""
	class Meta:
		model = models.Entry
		fields = ['text']
		labels= {'text':''}
		widgets={'text': forms.Textarea(attrs={'cols': 80})}