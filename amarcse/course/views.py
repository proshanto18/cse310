from django.shortcuts import  get_object_or_404
from .models import Course


# Create a new course
from django.shortcuts import render, redirect
from .forms import CourseForm

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successfully creating the course
    else:
        form = CourseForm()
    # Make sure to explicitly render courseform.html
    return render(request, 'courseform.html', {'form': form})


# Update an existing course
def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)  # Fetch the course or 404 if not found
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)  # Handle file uploads and update the course
        if form.is_valid():
            form.save()  # Save the updated course
            return redirect('course_list')  # Redirect to the course list after updating
    else:
        form = CourseForm(instance=course)  # Pre-populate the form with existing course data
    return render(request, 'courseform.html', {'form': form})

# Delete a course
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)  # Fetch the course or 404 if not found
    course.delete()  # Delete the course
    return render(request,'components/index.html')  # Redirect to the course list after deletion

# List all courses
def course_list(request):
    courses = Course.objects.all()  # Fetch all courses
    return render(request, 'course_list.html', {'courses': courses})
