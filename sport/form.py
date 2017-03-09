from django import forms
from django.contrib.auth.models import User
from .models import Playground


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=30, help_text="Please enter the category name.")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class PlaygroundForm(forms.ModelForm):

    class Meta:
        model = Playground
        fields = ['name_playground', 'description_playground', 'kind_of_sport', 'Location_playground']