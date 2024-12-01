from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('editor', views.code_editor, name='code_editor'),
    path('snippets/', views.view_snippets, name='view_snippets'),
    path('snippet/delete/<int:snippet_id>/', views.delete_snippet, name='delete_snippet'),
]

