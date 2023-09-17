from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignForm


def sign_up(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect()
    else:
        form = SignForm()
    return render(request, "users/users_form.html", {"form": form})

