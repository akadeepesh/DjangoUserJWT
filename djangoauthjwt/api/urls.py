from django.urls import path
from .views import (
    UserChangePasswordView,
    UserLoginView,
    UserProfileView,
    UserRegistrationView,
    UserLogoutView,
)
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("tokenize/", views.TokenizeSentence.as_view(), name="TokenizeSentence"),
    path("remove_stop_words/", views.RemoveStopwords.as_view(), name="RemoveStopwords"),
    # path("noise-reduction/", views.NoiseReduction.as_view(), name="NoiseReduction"),
    path('stemlem/', views.StemLemWords.as_view(), name='Stemming Lemmatization'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
