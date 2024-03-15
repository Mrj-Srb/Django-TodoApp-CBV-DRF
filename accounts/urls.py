from django.urls import path,include
from accounts import views

from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page="/"),name='logout'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('api/',include("accounts.api.urls"),name="api"),

]