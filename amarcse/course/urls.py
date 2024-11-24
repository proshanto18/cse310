from django.urls import path
from . import views

urlpatterns = [
    path('create_course/', views.add_course, name='create_course'),
    path('update/<int:course_id>/', views.update_course, name='update_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('', views.course_list, name='course_list'),  # Default route to list courses
]
