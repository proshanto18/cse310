from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from lectures.models import Lecture
from course.models import Course


def BASE(request):
    return render(request, 'base.html')


def INDEX(request):
    return render(request, 'components/index.html')


def ACADEMIC_COURSE(request):
    academic_courses = Course.objects.filter(category='academic')
    return render(request, 'components/academic_course.html', {'academic_courses': academic_courses})


def CAREER_COURSE(request):
    # Fetching all courses in the 'career' category
    career_courses = Course.objects.filter(category='career')

    # Rendering the 'career_course.html' template with the context
    return render(request, 'components/career_course.html', {'career_courses': career_courses})


def LECTURES(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lectures = Lecture.objects.filter(course=course)
    return render(request, 'components/lecture_list.html', {
        'lectures': lectures,
        'course': course
    })

def LEARNINGCONTENT(request):
    return render(request, 'components/learningcontent.html')


def EXERCISE(request):
    return render(request, 'components/exercise.html')


def REGISTER(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')

        # Basic validations
        if not uname or not email or not pw1 or not pw2:
            messages.error(request, "All fields are required.")
            return render(request, 'components/register.html')

        if pw1 != pw2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'components/register.html')

        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'components/register.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'components/register.html')

        # Create the user
        try:
            my_user = User.objects.create_user(username=uname, email=email, password=pw1)
            my_user.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('components/login.html')
        except Exception as e:
            messages.error(request, "An error occurred while creating the account.")
            return render(request, 'components/register.html')

    return render(request, 'components/register.html')


def LOGIN(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            login(request, user)
            return render(request, 'components/index.html',{'username':uname})
        else:
            return HttpResponse("Username or password is incorrect!")

    return render(request, 'components/login.html')


def LOGOUT(request):
    logout(request)
    return redirect("index")


def USER(request):
    return render(request, 'components/user.html')