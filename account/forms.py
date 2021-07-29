from django import forms
from django.utils.translation import gettext_lazy as _


class SignInForm(forms.Form):
    login = forms.CharField(max_length=20,
                            required=False,
                            widget=forms.TextInput(attrs={
                                'placeholder': _('Username or email'),
                            }))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'placeholder': _('Password'),
    }, ))
    remember_me = forms.BooleanField(label='Remember me', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'agree-term'
    }))
