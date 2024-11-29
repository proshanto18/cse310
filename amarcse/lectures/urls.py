from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/lectures/create/', views.create_lecture, name='create_lecture'),
    path('course/<int:course_id>/lectures/update/<int:p_id>/', views.update_lecture, name='update_lecture'),
    path('course/<int:course_id>/lectures/delete/<int:p_id>/', views.delete_lecture, name='delete_lecture'),
    path('course/<int:course_id>/lectures/', views.course_lectures, name='course_lectures'),
    path('lecture/<int:lecture_id>/exercise/create/', views.create_exercise, name='create_exercise'),
    path('exercise/<int:exercise_id>/update/', views.update_exercise, name='update_exercise'),
    path('exercise/<int:exercise_id>/delete/', views.delete_exercise, name='delete_exercise'),
]