from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
    path('products_view',views.products_view,name='view'),
    path('create_lecture',views.create_lecture,name='create-lecture'),
    path('update_lecture/<int:p_id>/', views.update_lecture, name='update-lecture'),
    path('delete_lecture/<int:p_id>/', views.delete_lecture, name='delete-lecture')


]