from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.utils import ErrorList, format_html, format_html_join
from account import models as app_models


class DivErrorList(ErrorList):
    def __init__(self, initlist=None, error_class='dsdsd'):
        super().__init__(initlist, error_class)

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return format_html(
            '<div class="{}">{}</div>',
            self.error_class,
            format_html_join('', '<div class="error">{}</div>', ((e,) for e in self))
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
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(SignUpForm, self).__init__(*args, **kwargs_new)

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
