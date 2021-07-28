from django.urls import path
from .views import Signup, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')

]
