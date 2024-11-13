from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.INDEX, name='index'),
    path('base', views.BASE, name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',views.REGISTER,name='register'),
    path('login/',views.LOGIN,name='login'),
    path('logout/', views.LOGOUT, name='logout'),
    

]