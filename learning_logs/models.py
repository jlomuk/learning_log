from django.db import models


class Topic(models.Model):
	"""Тема, которую изучает пользователь """

	text = models.CharField(max_length=200, verbose_name='Тема')
	data_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name='Тема'
		verbose_name_plural = 'Темы'

	def __str__(self):
		"""Возвращает строковое представление модели"""
		return self.text


class Entry(models.Model):
	"""Информация изученная пользователем по теме"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	data_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

	class Meta:
		verbose_name='Запись'
		verbose_name_plural='Записи'

	def __str__(self):
		"""Возвращает строковое представление модели"""
		return f'{self.text[:40]}...'