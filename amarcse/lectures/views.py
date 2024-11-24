from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Lecture
from .forms import LectureForm
from course.models import Course



# Create a new lecture
def create_lecture(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.course = course
            lecture.save()
            return redirect('course_lectures', course_id=course.id)
    else:
        form = LectureForm()
    return render(request, 'courseform.html', {'form': form, 'course': course})

# Update an existing lecture
def update_lecture(request, course_id, p_id):
    course = get_object_or_404(Course, id=course_id)
    lecture = get_object_or_404(Lecture, id=p_id, course=course)
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES, instance=lecture)
        if form.is_valid():
            form.save()
            return redirect('course_lectures', course_id=course.id)
    else:
        form = LectureForm(instance=lecture)
    return render(request, 'courseform.html', {'form': form, 'course': course})


# Delete a lecture
def delete_lecture(request, course_id, p_id):
    course = get_object_or_404(Course, id=course_id)
    lecture = get_object_or_404(Lecture, id=p_id, course=course)
    lecture.delete()
    return redirect('course_lectures', course_id=course.id)


# A view to display all lectures (can be used for a lecture list page)
def course_lectures(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lectures = course.lectures.all()  # Use the related_name from the Lecture model
    return render(request, 'components/lecture_list.html', {'lectures': lectures, 'course': course})


# Placeholder view for products (not related to CRUD operations)
def products_view(request):
    return render(request, 'products_view.html')