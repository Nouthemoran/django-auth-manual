from django.urls import path
from . views import RegisterView, Login

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', .as_view())
]
