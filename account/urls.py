from django.urls import path, include
from django.views.generic import RedirectView

from account import views

app_name = 'account'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='account:signin')),
    path('sign-in/', views.SignInFormView.as_view(), name='signin'),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('account/<str:slug>/', views.AccountDetailView.as_view(), name='detail'),
    # path('login/', views.login, name='login_form'),
]
