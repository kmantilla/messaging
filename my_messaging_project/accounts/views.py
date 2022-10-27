# accounts/views.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"

class UserUpdateView(generic.UpdateView):
    # form_class = UserChangeForm
    # success_url = reverse_lazy("home")
    # template_name = "account/update.html"
    model = CustomUser
    fields = ['username']
    success_url = reverse_lazy("home")
    template_name = "account/update.html"

