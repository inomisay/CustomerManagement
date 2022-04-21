from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='registration/password/password_change.html')),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password/password_change_done.html')),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password/password_reset.html')), #still django template 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password/password_reset_done.html')),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password/password_reset_confirm.html')),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password/password_reset_complete.html')),
    path('create-customer', views.create_customer, name='create_customer'),
]
