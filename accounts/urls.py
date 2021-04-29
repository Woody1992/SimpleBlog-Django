from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, PwdResetForm, PwdResetConfirmForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=UserLoginForm
        ), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html",
        form_class=PwdResetForm
        ), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        form_class=PwdResetConfirmForm
        ), name="pwdresetconfirm"),
    path('profile/', views.profile, name='profile'),
    path('register/', views.accounts_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
]
