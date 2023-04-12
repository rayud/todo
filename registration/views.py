from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Userlogin(request):
    if request.method == 'POST':
        user = auth.authenticate(password=request.POST['password1'], username=request.POST['username'])

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request,'username or password is incorrect!')
            return render(request, 'registration/login.html')

    else:
        return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            try:
                User.objects.get(username=request.POST['username'], email=request.POST['email'])
                messages.error('username and email was already taken')
                return redirect('register')

            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'] ,password=request.POST['password1'])
                user.save()
                auth.login(request, user)
                return redirect('index')
        else:
            messages.error('password did not match')
            return render(request, 'registration/register.html')
    else:
        return render(request, 'registration/register.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'You have successfully Logout')
    return redirect ('index')
