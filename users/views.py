from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, CreateView, TemplateView, DetailView

from braces.views import SelectRelatedMixin

from . import forms

class DashboardView(LoginRequiredMixin, DetailView, SelectRelatedMixin):
  model = User
  select_related = ('thoughts',)
  template_name = 'users/dashboard.html'

  def get_object(self, queryset=None):
    return self.request.user

class LogoutView(LoginRequiredMixin, FormView):
  form_class = forms.LogoutForm
  template_name = 'users/logout.html'

  def form_valid(self, form):
    logout(self.request)
    return HttpResponseRedirect(reverse('home'))

class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'users/signup.html'
  success_url = 'users:dashboard'