from django.urls import path
from .views import (
    UserChangePasswordView,
    UserLoginView,
    UserProfileView,
    UserRegistrationView,
    UserLogoutView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
