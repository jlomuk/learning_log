from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_homepage, name='homepage'),
    path('topics/<int:pk>', views.get_topic_detail, name='topic_detail'),
    path('topics/', views.get_topics, name='topics'),
]
