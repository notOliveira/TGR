from django import forms
from django.contrib.auth.models import User
from .models import Profile, Quiz
from django.contrib.auth.forms import UserCreationForm
from .constants import Q1_CHOICES, Q2_CHOICES, Q3_CHOICES, Q4_CHOICES, Q5_CHOICES, Q6_CHOICES, Q7_CHOICES

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
            'q7'
        ]

    def clean_q1(self):
        q1_value = self.cleaned_data['q1']
        # Substitua Q1_CHOICES pelos seus valores reais de choices para q1
        valid_choices = [choice[0] for choice in Q1_CHOICES]
        
        if q1_value not in valid_choices:
            raise forms.ValidationError("Valor inválido para q1.")
        
        return q1_value

    def clean_q2(self):
        q2_value = self.cleaned_data['q2']
        # Substitua Q2_CHOICES pelos seus valores reais de choices para q2
        valid_choices = [choice[0] for choice in Q2_CHOICES]
        
        if q2_value not in valid_choices:
            raise forms.ValidationError("Valor inválido para q2.")
        
        return q2_value

    def clean_q3(self):
        q3_value = self.cleaned_data['q3']
        # Substitua Q3_CHOICES pelos seus valores reais de choices para q3
        valid_choices = [choice[0] for choice in Q3_CHOICES]
        
        if q3_value not in valid_choices:
            raise forms.ValidationError("Valor inválido para q3.")
        
        return q3_value

    def clean_q4(self):
        q4_value = self.cleaned_data['q4']
        # Substitua Q4_CHOICES pelos seus valores reais de choices para q4
        valid_choices = [choice[0] for choice in Q4_CHOICES]
        
        if q4_value not in valid_choices:
            raise forms.ValidationError("Valor inválido para q4.")
        
        return q4_value

    def clean_q5(self):
        q5_value = self.cleaned_data['q5']
        # Substitua Q5_CHOICES pelos seus valores reais de choices para q5
        valid_choices = [choice[0] for choice in Q5_CHOICES]
        
        if q5_value not in valid_choices:
            raise forms.ValidationError("Valor inválido para q5.")
        
        return q5_value

    def clean_q6(self):
        q6_value = self.cleaned_data['q6']
        # Substitua Q6_CHOICES pelos seus valores reais de choices para q6
        valid_choices = [choice[0] for choice in Q6_CHOICES]
        
        if q6_value not in valid_choices:
            raise forms.ValidationError("Valor inválido para q6.")
        
        return q6_value

    def clean_q7(self):
        q7_value = self.cleaned_data['q7']
        # Substitua Q7_CHOICES pelos seus valores reais de choices para q7
        valid_choices = [choice[0] for choice in Q7_CHOICES]
        
        if q7_value not in valid_choices:
            raise forms.ValidationError("Valor inválido para q7.")
        
        return q7_value