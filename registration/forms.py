from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Prolni tasdiqlang',
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'confirm_password', 'role']

        labels = {
            'username': _('Foydalanuvchi nomi'),
            'password': _('Parol'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError(f"Foydalanuvchi '{username}' ro'yxatdan o'tgan !", code='invalid')
        return username

    def clean(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            confirmed_password = self.cleaned_data['confirm_password']
            if confirmed_password != password:
                raise ValidationError('Parol mos kelmadi !', code='invalid')
        return self.cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        labels = {
            'username': _('Foydalanuvchi nomi'),
            'password': _('Parol'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        if 'username' in self.cleaned_data and 'password' in self.cleaned_data:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = CustomUser.objects.filter(username=username).first()
            if not user:
                raise ValidationError(f"Foydalanuvchi '{username}' tizimda ro'yxatdan o'tmagan !", code='invalid')
            if user:
                if not user.check_password(password):
                    raise ValidationError(f"Parol xato !", code='invalid')
        return self.cleaned_data
