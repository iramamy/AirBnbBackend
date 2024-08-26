from django.urls import path

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from . import api

urlpatterns = [
    path("useremail/", api.email_list, name="email_list"),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("<uuid:pk>/", api.landlord_detail, name="api_landlord_detail"),
    path("myreservations/", api.reservation_list, name="api_reservation_list"),
]
