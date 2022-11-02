from django.urls import path
from .views import register, profile
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import PasswordResetEmailCheck

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"),  name="login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"),  name="logout"),
    path("profile/", profile, name="profile"),
    path("password-change/", PasswordChangeView.as_view(template_name="users/password_change_form.html"), name="password_change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
    path("password-reset/", PasswordResetView.as_view(template_name="users/password_reset_email.html", form_class = PasswordResetEmailCheck), name="password_reset"),
    path("password-reset-done/", PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),

]
