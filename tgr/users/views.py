from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=nickname, password=password)
            login(request, user)
            return redirect('home')
    else:
        messages.error(request, ("Ocorreu um erro! Por favor tente novamente."))
        form = UserCreationForm()
    return render(
        request, 'users/register.html', {
            'form': form
            }
        )

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