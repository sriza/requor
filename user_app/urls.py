from django.urls import path, include
from .views import loginauth,logout

urlpatterns = [
    path("", loginauth, name="login"),
    path("logout/", logout, name="logout"),
]
