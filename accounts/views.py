from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

from django.core.mail import send_mail

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
