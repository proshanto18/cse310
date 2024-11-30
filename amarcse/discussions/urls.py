from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from .import views

urlpatterns = [
   path('discussions/',views.discussions, name='discussions')

]

