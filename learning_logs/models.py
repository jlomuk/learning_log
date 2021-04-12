from django.db import models


class Topic(models.Model):
	"""Тема, которую изучает пользователь """
	class Meta:
		verbose_name='Тема'
		verbose_name_plural = 'Темы'

	text = models.CharField(max_length=200, verbose_name='Тема')
	data_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	def __str__(self):
		"""Возвращает строковое представление модели"""
		return self.text