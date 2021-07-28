from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# Create your views here.
class LoginFormView(generic.FormView):
    template_name = 'account/signin.html'
    # form_class = ContactForm
    success_url = '/account/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)


def login(request):
    return HttpResponse('login')
