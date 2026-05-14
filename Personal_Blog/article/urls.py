from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_Blog, name='add_Blog'),
    path('edit/<int:blog_id>/', views.edit_Blog, name='edit_Blog'),
    path('delete/<int:blog_id>/', views.delete_Blog, name='delete_Blog'),
]