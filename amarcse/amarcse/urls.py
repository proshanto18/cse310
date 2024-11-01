from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.INDEX, name='index'),
    path('base', views.BASE, name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',views.REGISTER,name='register'),

]