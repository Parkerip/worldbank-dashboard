from django.urls import path
from .views import hello_view, worldbank_data
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("hello/", hello_view, name="hello"),
    path("worldbank/", worldbank_data, name="worldbank"),
    path("login/", obtain_auth_token, name="login"),  # 👈 new
]
