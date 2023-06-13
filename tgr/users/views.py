from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_user(request):
    return render(request, 'users/register.html')

def login_user(request):
        if request.method == "POST":
            nickname = request.POST['nickname']
            password = request.POST['password']
            user = authenticate(request, username=nickname, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, ("Ocorreu um erro! Por favor tente novamente."))
                return redirect('login')
        else:
            return render(request, 'users/login.html', {})

def logout_user(request):
        return render(request, 'users/logout.html')