from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UsersUpdateForm

def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=nickname, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
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
                messages.error(request, "Ocorreu um erro! Por favor tente novamente.")
                return redirect('login')
        else:
            messages.error(request, '')
            return render(request, 'users/login.html', {})

def logout_user(request):
    context = {
    }
    return render(request, 'users/logout.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UsersUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Perfil atualizado")
            return redirect('profile')
    else:
        user_form = UsersUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'users/profile.html', context)