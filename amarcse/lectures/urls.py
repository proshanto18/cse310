from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/lectures/create/', views.create_lecture, name='create_lecture'),
    path('course/<int:course_id>/lectures/update/<int:p_id>/', views.update_lecture, name='update_lecture'),
    path('course/<int:course_id>/lectures/delete/<int:p_id>/', views.delete_lecture, name='delete_lecture'),
    path('course/<int:course_id>/lectures/', views.course_lectures, name='course_lectures'),
]
