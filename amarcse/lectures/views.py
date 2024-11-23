from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Lecture
from .forms import LectureForm

# Create a new lecture
def create_lecture(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)  # Ensure files are also handled
        if form.is_valid():
            form.save()
            return redirect('career_course')  # Redirect to a lecture list or detail view after saving
    else:
        form = LectureForm()
    return render(request, 'form.html', {'form': form})

# Update an existing lecture
def update_lecture(request, p_id):
    lecture = get_object_or_404(Lecture, pk=p_id)  # Get the lecture, or 404 if not found
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES, instance=lecture)  # Ensure files are handled
        if form.is_valid():
            form.save()
            return redirect('career_course')  # Redirect to a lecture list or detail view after updating
    else:
        form = LectureForm(instance=lecture)
    return render(request, 'form.html', {'form': form})

# Delete a lecture
def delete_lecture(request, p_id):
    lecture = get_object_or_404(Lecture, pk=p_id)  # Ensure the lecture exists
    lecture.delete()
    return redirect('career_course')  # Redirect after deletion to avoid showing a "deleted" page

# A view to display all lectures (can be used for a lecture list page)
def lecture_list(request):
    lectures = Lecture.objects.all()  # Fetch all lectures
    return render(request, 'lecture_list.html', {'lectures': lectures})

# Placeholder view for products (not related to CRUD operations)
def products_view(request):
    return render(request, 'products_view.html')