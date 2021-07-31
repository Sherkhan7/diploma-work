from django import forms
from django.utils.translation import gettext_lazy as _

from account import models as app_models


class SignInForm(forms.Form):
    login = forms.CharField(max_length=20,
                            required=False,
                            widget=forms.TextInput(attrs={
                                'placeholder': _('Username or email'),
                            }))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'placeholder': _('Password'),
    }, ))
    remember_me = forms.BooleanField(label=_('Remember me'), required=False, widget=forms.CheckboxInput(attrs={
        'class': 'agree-term'
    }))


class SignUpForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    # email = forms.EmailField(max_length=30, required=True, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={
        'placeholder': _('Password')
    }))
    password2 = forms.CharField(label='Repeat Password', required=False, widget=forms.PasswordInput(attrs={
        'placeholder': _('Repeat your password')
    }))
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': _('Username')
    }))

    class Meta:
        model = app_models.User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': _('First name')
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': _('Last name')
            }),
            'username': forms.TextInput(attrs={
                'placeholder': _('Username')
            }),
            'email': forms.TextInput(attrs={
                'placeholder': _('Your email')
            }),
        }
