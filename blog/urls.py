from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('manage_subscribers/', views.manage_subscribers, name='manage_subscribers'),
]



