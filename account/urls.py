from django.urls import path, include
from django.views.generic import RedirectView

from account import views

app_name = 'account'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='signin')),
    path('sign_in/', views.SignInFormView.as_view(), name='signin'),
    path('sign_up/', views.SignUpView.as_view(), name='signup'),
    # path('login/', views.login, name='login_form'),
]
