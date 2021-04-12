from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_homepage, name='homepage'),
    path('topics/<int:pk>', views.get_topic_detail, name='topic_detail'),
    path('topics/', views.get_topics, name='topics'),
    path('new_topic/', views.add_new_topic, name='new_topic'),
    path('new_entry/<int:pk>', views.add_new_entry, name='new_entry'),
     path('edit_entry/<int:pk>', views.edit_entry, name='edit_entry'),
]
