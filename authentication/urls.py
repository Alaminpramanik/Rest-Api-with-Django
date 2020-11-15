from django.urls import path
from .views import login,register,RegisterView, LoginView


urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('registerview/', RegisterView.as_view()),
    path('voginview/', LoginView.as_view()),
]    