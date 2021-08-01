from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from account import forms
from account.models import User


class SignInFormView(generic.FormView):
    template_name = 'account/signin.html'
    # success_url = '/account/'
    form_class = forms.SignInForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form_heading'] = 'Sign in to account'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print('weqwewq')
        print(form.is_valid(), 'ddddddddddddddddddd')
        return super().form_valid(form)


class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'account/signup.html'

# def login(request):
#     return HttpResponse('login')
