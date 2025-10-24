from django.urls import path
from user.views import (
    UserRegistrationView, UserLoginView
)


app_name = 'user'


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
