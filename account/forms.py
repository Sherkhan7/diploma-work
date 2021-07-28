from django import forms
from django.utils.translation import gettext_lazy as _


class SignInForm(forms.Form):
    username_email = forms.CharField(label='Usernam or email', max_length=50, help_text="Enter 6 digit roll number")
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'placeholder': _('Password'),
        }
    ))
