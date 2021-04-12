from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_homepage, name='homepage'),
    path('topics/', views.get_homepage, name='topics'),
]
