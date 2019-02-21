from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Login(request):
    return render(request, 'login/login.html')

def Search(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    user = authenticate(username = username, password = password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('login/success.html')
        else:
            return render_to_response('login/failure.html')
    else:
        return render_to_response('login/failure1.html')

def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        CompareFlag = False
        errors = []

        if not request.POST.get('name'):
            errors.append('Please enter name')
        else:
            name = request.POST.get('name')
        if not request.POST.get('password1'):
            errors.append('Please enter password1')
        else:
            password1 = request.POST.get('password1')
        if not request.POST.get('password2'):
            errors.append('Please enter password2')

        if password1 is not None and password2 is not None:
            if password1 == password2:
                CompareFlag = True
            else:
                errors.append('password2 is different password')

        filterResult = User.objects.filter(username = name)
        if len(filterResult) > 0:
            errors.append('The user has exits!')
            return render_to_response('login/login.html', {'errors': errors})

        if name is not None and password1 is not None and password2 is not None and CompareFlag:
            user = User()
            user.username = name
            user.set_password(password1)
            user.save()
            return HttpResponseRedirect('/user/login')
        return render_to_response('login/register.html', {'errors': errors})

def Register(request):
    return render(request, 'login/register.html')

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login')

