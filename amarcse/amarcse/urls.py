from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from . import settings
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.INDEX, name='index'),
    path('base', views.BASE, name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',views.REGISTER,name='register'),
    path('login/',views.LOGIN,name='login'),
    path('logout/', views.LOGOUT, name='logout'),
    path('user/', views.USER, name='user'),
    path('academic_course/', views.ACADEMIC_COURSE, name='academic_course'),
    path('career_course/', views.CAREER_COURSE, name='career_course'),
    path('course/<int:course_id>/lectures/', views.LECTURES, name='lecture_list'),
    path('exercise/', views.EXERCISE, name='exercise'),
    path('lectures/',include('lectures.urls')),
    path('course/',include('course.urls')),
    path('blog/',include('blog.urls')),
    path('blog/',include('userprofile.urls')),
path('code_editor/',include('code_editor.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)