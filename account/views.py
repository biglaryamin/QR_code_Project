from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

from .forms import NewUserForm

def show_profile(request):
    username = request.user.username
    email = request.user.email
    full_name = request.user.get_full_name()
    return render(request, "account/profile.html", {"username":username,
                            "email":email,"full_name":full_name})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main_app:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})