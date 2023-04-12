from django.forms import CheckboxInput, ModelForm, PasswordInput, TextInput
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 40%;,color:white'
            
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
            'class': 'form-control text-input'
            }),
            'email': TextInput(attrs={
            'class': 'form-control text-input'
            }),
            'password1': PasswordInput(attrs={
            'class': 'form-control pass-input'
            }),
            'password2': TextInput(attrs={
            'class': 'form-control pass-input'
            }),
        }

