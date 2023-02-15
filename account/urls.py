from django.contrib.auth import views
from django.urls import path
from .views import show_profile, register_request


app_name="account"
urlpatterns=[
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path("register/", register_request, name="register"),

    path('profile', show_profile, name='show_profile'),
]