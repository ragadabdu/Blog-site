from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

INPUT_CLASSES = 'w-full h-10 rounded-lg px-4'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : ('Username'),
        'class' : INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : ('password'),
        'class' : INPUT_CLASSES
    }))

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : ('Username'),
        'class' : INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : ('email'),
        'class' : INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : ('password'),
        'class' : INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : ('repeat password'),
        'class' : INPUT_CLASSES
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

