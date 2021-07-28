from django.urls import path, include
from django.views.generic import RedirectView

from account import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login_form')),
    # path('login/', views.login, name='login_form'),
    path('login/', views.LoginFormView.as_view(), name='login_form'),
]
