from django.shortcuts import render
from django.contrib.auth.models import User


def show_profile(request):
    username = request.user.username
    email = request.user.email
    full_name = request.user.get_full_name()
    return render(request, "account/profile.html", {"username":username,
                            "email":email,"full_name":full_name})