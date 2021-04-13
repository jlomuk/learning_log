from django.http import Http404


def check_topic_owner(request, topic):
	"""Проверяет, является ли пользователь владельцем запрошенной темы"""
	if topic.owner != request.user:
		raise Http404