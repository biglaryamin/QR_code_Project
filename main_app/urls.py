from django.urls import path
from .views import application_qr_code_demo


urlpatterns = [
    path('test', application_qr_code_demo),
]
