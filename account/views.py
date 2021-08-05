from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views import generic

from account import forms
from account.models import User


class SignInFormView(generic.FormView):
    template_name = 'account/signin.html'
    form_class = forms.SignInForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form_heading'] = 'Sign in to account'
        return context


class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'account/signup.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(user.get_absolute_url())


class AccountDetailView(generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'account/accout.html'

# def login(request):
#     return HttpResponse('login')
