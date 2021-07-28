from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from account import forms


class SignInFormView(generic.FormView):
    template_name = 'account/signin.html'
    form_class = forms.SignInForm
    success_url = '/account/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)


class SignUpView(generic.CreateView):
    template_name = 'account/signup.html'
    # form_class = forms.SignInForm


def login(request):
    return HttpResponse('login')
