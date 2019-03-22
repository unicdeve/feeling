from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import SetHeadlineMixin

from .. import forms

class Create(LoginRequiredMixin, SetHeadlineMixin, CreateView):
  form_class = forms.FamilyForm
  headline = 'Create Family'
  success_url = reverse_lazy("users:dashboard")
  template_name = 'families/form.html'

  def form_valid(self, form):
    form.instance.created_by = self.request.user
    response = super().form_valid(form)
    self.object.members.add(self.request.user)
    return response

class Update(LoginRequiredMixin, SetHeadlineMixin, UpdateView):
  form_class = forms.FamilyForm
  template_name = 'families/form.html'

  def get_queryset(self):
    return self.request.user.families.all()

  def get_headline(self):
    return f'Edit {self.object.name}'

  def get_success_url(self):
    return reverse('groups:families:detail', kwargs={'slug': self.object.slug})


class Detail(LoginRequiredMixin, DetailView):
  template_name = 'families/detail.html'

  def get_queryset(self):
    return self.request.user.families.all()

