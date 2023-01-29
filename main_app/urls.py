from django.urls import path
from .views import test, temp

app_name = "main_app"
urlpatterns = [
    path('home', test, name="home"),
    path('temp', temp, name="temp"),
]
