from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import SetHeadlineMixin

from .. import forms
from ..models import Company

class Create(LoginRequiredMixin, SetHeadlineMixin, CreateView):
  form_class = forms.CompanyForm
  headline = 'Create Company'
  success_url = reverse_lazy("users:dashboard")
  template_name = 'companies/form.html'

  def form_valid(self, form):
    form.instance.created_by = self.request.user
    response = super().form_valid(form)
    self.object.members.add(self.request.user)
    return response

class Update(LoginRequiredMixin, SetHeadlineMixin, UpdateView):
  form_class = forms.CompanyForm
  success_url = reverse_lazy("users:dashboard")
  template_name = 'companies/form.html'

  def get_queryset(self):
    return self.request.user.companies.all()

  def get_headline(self):
    return f'Edit {self.object.name}'


class Detail(LoginRequiredMixin, DetailView):
  template_name = 'companies/detail.html'

  def get_queryset(self):
    return self.request.user.companies.all()

