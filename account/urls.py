from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import APILogoutView, MyTokenObtainPairView

urlpatterns = [
    path('login/api/', MyTokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('logout/api/', APILogoutView.as_view(), name='logout_view'),
]
