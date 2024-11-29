from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import LectureForm,ExerciseForm
from course.models import Course
from .models import Lecture, Exercise





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
    return render(request, 'form.html', {'form': form, 'course': course})


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



def delete_lecture(request, course_id, p_id):
    course = get_object_or_404(Course, id=course_id)
    lecture = get_object_or_404(Lecture, id=p_id, course=course)
    lecture.delete()
    return redirect('course_lectures', course_id=course.id)



def course_lectures(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lectures = course.lectures.all()  # Use the related_name from the Lecture model
    return render(request, 'components/lecture_list.html', {'lectures': lectures, 'course': course})



def products_view(request):
    return render(request, 'products_view.html')




def create_exercise(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.lecture = lecture
            exercise.save()
            return redirect('lecture_list', course_id=lecture.course.id)
    else:
        form = ExerciseForm()
    return render(request, 'exercise_form.html', {'form': form})

def update_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('lecture_list', course_id=exercise.lecture.course.id)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'exercise_form.html', {'form': form})

def delete_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    course_id = exercise.lecture.course.id
    if request.method == 'POST':
        exercise.delete()
        return redirect('lecture_list', course_id=course_id)
    return render(request, 'exercise_delete_form.html', {'exercise': exercise})