from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LectureForm
from .models import Lecture


# Create your views here.
def create_lecture(request):
    if request.method=='POST':
        form=LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
    else:
        form=LectureForm()
    return render(request, template_name='form.html',context={'form':form})



def update_lecture(request,p_id):
    p=LectureForm.objects.get(pk=p_id)
    if request.method=='POST':
        form=LectureForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
    else:
        form=LectureForm(instance=p)
    return render(request, template_name='form.html',context={'form':form})

def delete_lecture(request,p_id):
    Lecture.objects.get(pk=p_id).delete()
    return render(request,template_name='index.html')

def products_view(request):
    return render(request,template_name='products_view.html')
