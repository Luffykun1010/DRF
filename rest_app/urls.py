from .views import LoginView
from django.urls import path
urlpatterns = [
    path('api/login', LoginView.as_view(), name='user-login'),
]