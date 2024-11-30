from django.shortcuts import render

# Create your views here.

def discussions(request):
    return render(request,'discussions/discussions.html')
