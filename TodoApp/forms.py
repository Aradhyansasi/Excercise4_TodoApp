from django import forms
from TodoApp.models import Todo, User
from django.contrib.auth.forms import UserCreationForm




class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_name','status']
