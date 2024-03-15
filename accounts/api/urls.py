from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns =[
    # token login
    path('token/login/',views.CustomLoginAuthToken.as_view(),name="token-login"),
    
    # token logout
    path('token/logout/',views.CustomLogoutAuthToken.as_view(),name="token-logout"),

    # jwt create
    path('jwt/create/',TokenObtainPairView.as_view(),name="jwt-create"),

    # jwt refresh
    path('jwt/refresh/',TokenRefreshView.as_view(),name="jwt-refresh"),

    # jwt verify
    path('jwt/verify/',TokenRefreshView.as_view(),name="jwt-verify"),

]