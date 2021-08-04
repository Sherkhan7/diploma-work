from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.utils import ErrorList, format_html, format_html_join
from django.core.exceptions import ValidationError

from account import models as app_models


class DivErrorList(ErrorList):
    def __init__(self, initlist=None, error_class='list'):
        super(DivErrorList, self).__init__(initlist, error_class)

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return format_html(
            '<div class="{}">{}</div>',
            self.error_class,
            format_html_join('', '<div class="error">* {}</div>', ((e,) for e in self))
        )


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
    """
        def __init__(self, *args, **kwargs):
            kwargs_new = {'error_class': DivErrorList}
            kwargs_new.update(kwargs)
            super().__init__(*args, **kwargs_new)
    """

    # first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    # email = forms.EmailField(max_length=30, required=True, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': _('Password')
    }))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={
        'placeholder': _('Repeat your password')
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Username')
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': _('Your email')
    }))
    role = forms.ChoiceField(label='User type', choices=app_models.User.ROLE_CHOICES, widget=forms.Select(attrs={
        'class': 'select'}
    ))

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
        }

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']

        if password1 != password2:
            raise ValidationError("Password does not match")

        return cleaned_data
