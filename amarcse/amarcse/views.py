from django.shortcuts import redirect,render

def BASE(request):
    return render(request,'base.html')

def REGISTER(request):
    return render(request,'login_register/register.html')