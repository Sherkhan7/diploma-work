from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import LoginForm, SignupForm


# Create your views here.

class Signup(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('profile')
    success_message = "Your profile was created successfully"

    # def post(self, request, *args, **kwargs):
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         print('ewqeqeqwe')
    #         new_user = form.save(commit=False)
    #         new_user.username = form.cleaned_data['username']
    #         new_user.set_password(form.cleaned_data['password'])
    #         new_user.save()
    #         user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    #         login(request, user)
    #         return redirect('profile')
    #     else:
    #         form = SignupForm()
    #
    #     return render(request, self.template_name, {'form': form})
    


class Login(generic.FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
            return redirect('profile')
        else:
            form = LoginForm()

        return render(request, self.template_name, {'form': form})
