from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
        path('create/', views.create_lecture, name='create_lecture'),
    path('update/<int:p_id>/', views.update_lecture, name='update_lecture'),
    path('delete/<int:p_id>/', views.delete_lecture, name='delete_lecture'),
    path('lectures/', views.lecture_list, name='lecture_list'),
    path('products/', views.products_view, name='products_view')


]