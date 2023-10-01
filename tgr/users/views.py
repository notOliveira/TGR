from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UsersUpdateForm, QuizForm
from .models import Quiz

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

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
            messages.error(request, "Usuário não existe! Por favor tente novamente.")
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
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('profile')
    else:
        user_form = UsersUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'users/profile.html', context)

def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Redefinição de senha'
                    email_template_name = 'users/reset_password_email.txt'
                    parameters = {
                        'username': user.username,
                        'email': user.email,
                        # Mudar para domínio de produção
                        'domain': 'notoliveira.pythonanywhere.com',
                        'site_name': 'TGR',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, '', [user.email], fail_silently=False)
                    except:
                        return HttpResponse('Invalid Header')
                    return redirect('password_reset_done')
    else:
        password_form = PasswordResetForm()
    context = {
        'password_form': password_form  
    }
    return render(request, 'users/password_reset.html', context)

@login_required
def quiz(request):
    quiz, created = Quiz.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        print(request)
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuizForm(instance=quiz)
    context = {
        'form': form
    }
    return render(request, 'users/quiz.html', context)

def pre_quiz(request):  
    context = {
        'footer': True
    }    
    return render(request, 'users/pre_quiz.html', context)