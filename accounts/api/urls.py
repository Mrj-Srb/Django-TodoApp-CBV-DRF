from django.urls import path
from . import views

urlpatterns =[
    # token login
    path('token/login/',views.CustomLoginAuthToken.as_view(),name="token-login"),
    
    # token logout
    path('token/logout/',views.CustomLogoutAuthToken.as_view(),name="token-logout"),

    #jwt create

    # jwt refresh

    # jwt verify
]