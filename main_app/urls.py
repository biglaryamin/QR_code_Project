from django.urls import path
from .views import test

app_name = "main_app"
urlpatterns = [
    path('home', test, name="home"),
]
