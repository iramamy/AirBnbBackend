from django.urls import path

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from . import api

urlpatterns = [
    path("user_list/", api.user_list, name="user_list"),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("<uuid:pk>/", api.landlord_detail, name="api_landlord_detail"),
    path("myreservations/", api.reservation_list, name="api_reservation_list"),
    path("user/<uuid:pk>/", api.user_detail, name="api_user_detail"),
    path("editprofile/", api.edit_user_profile, name="api_edit_user_profile"),
    path("changepassword/", api.change_password, name="api_change_password"),
]
