from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import SetHeadlineMixin

from .. import models

from .. import forms

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
  template_name = 'companies/form.html'

  def get_queryset(self):
    return self.request.user.companies.all()

  def get_headline(self):
    return f'Edit {self.object.name}'

  def get_success_url(self):
    return reverse('groups:companies:detail', kwargs={'slug': self.object.slug})


class Detail(LoginRequiredMixin, FormView):
  form_class = forms.CompanyInviteForm
  template_name = 'companies/detail.html'

  def get_queryset(self):
    return self.request.user.companies.all()

  def get_object(self):
    self.object = self.request.user.companies.get(slug=self.kwargs.get('slug'))
    return self.object

  def get_success_url(self):
    self.get_object()
    return reverse('groups:companies:detail', kwargs={'slug': self.object.slug})

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)    
    context['object'] = self.get_object()
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    models.CompanyInvite.objects.create(from_user=self.request.user, to_user=form.invitee, company=self.get_object())
    return response

