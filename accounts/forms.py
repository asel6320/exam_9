from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        error_messages={'required': 'First name is required'}
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        error_messages={'required': 'Last name is required'}
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']

