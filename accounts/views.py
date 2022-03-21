from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .forms import CreateUserForm, ChangePasswordForm, LoginForm


def register_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                print("new user is being saved")
                form.save()
                messages.success(
                    request, f"Account was created for {request.POST.get('username')}"
                )
                return redirect("accounts:login")

        context = {"form": form}
        return render(request, "accounts/register.html", context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:

        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect("home")
            else:
                messages.info(request, "Username or password is incorrect...")

        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)


@login_required(login_url="accounts:login")
def logout_user(request):
    logout(request)
    return redirect("home")


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/password_change_form.html"
    form_class = ChangePasswordForm
    success_url = reverse_lazy("accounts:password_change_done")
    login_url = reverse_lazy('accounts:login')


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"
    login_url = reverse_lazy('accounts:login')

