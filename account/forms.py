from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.utils import ErrorList, format_html, format_html_join
from django.contrib.auth.forms import UserCreationForm

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


class SignUpForm(UserCreationForm):
    """
        def __init__(self, *args, **kwargs):
            kwargs_new = {'error_class': DivErrorList}
            kwargs_new.update(kwargs)
            super().__init__(*args, **kwargs_new)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.pop('autofocus', None)

    use_required_attribute = False
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder': _('Your password')
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder': _("Password confirmation")
        }),
        strip=False,
    )

    class Meta:
        model = app_models.User
        fields = ('first_name', 'last_name', 'username', 'email', 'role')
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
            'email': forms.EmailInput(attrs={
                'placeholder': _('Your email'),
            }),
        }
