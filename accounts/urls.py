from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('password_change/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_change_success.html'), name='password_done'),
    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_forms.html', success_url = reverse_lazy('password_done')), name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name = 'registration/password_reset_forms.html'), name='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'registration/password_reset_success.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'registration/password_reset_change.html'), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'registration/password_reset_completes.html'), name = 'password_reset_complete')
]