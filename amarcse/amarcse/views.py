from django.shortcuts import redirect,render

def BASE(request):
    return render(request,'base.html')

def INDEX(request):
    return render(request,'components/index.html')

def REGISTER(request):
    return render(request,'components/register.html')

def LOGIN(request):
    return render(request,'components/login.html')
