from django import forms
from django.contrib.auth.models import User
from .models import Profile, Quiz
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UsersUpdateForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)
        
    class Meta:
        model = User
        fields = ['username', 'email']
        
        # Passando atributos para um formulário
    def __init__(self,*args,**kwargs):
        super(UsersUpdateForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'text-muted'})

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
            'q6',
            'q7',
            'q8',
            'q9',
            'q10',
            ]