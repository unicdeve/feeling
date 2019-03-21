from django import forms
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms

class CompanyCreate(LoginRequiredMixin, CreateView):
  form_class = forms.CompanyForm
  success_url = reverse_lazy("users:dashboard")
  template_name = 'companies/company_form.html'

  def form_valid(self, form):
    form.instance.created_by = self.request.user
    response = super().form_valid(form)
    self.object.members.add(self.request.user)
    self.object.members.save()
    return response
