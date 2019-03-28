from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import (
  CreateView, 
  UpdateView, 
  DetailView,
  ListView,
  RedirectView,
  FormView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import SetHeadlineMixin

from .. import models

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


class Detail(LoginRequiredMixin, FormView):
  form_class = forms.FamilyInviteForm
  template_name = 'families/detail.html'

  def get_queryset(self):
    return self.request.user.families.all()

  def get_object(self):
    self.object = self.request.user.families.get(slug=self.kwargs.get('slug'))
    return self.object

  def get_success_url(self):
    self.get_object()
    return reverse('groups:families:detail', kwargs={'slug': self.object.slug})

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)    
    context['object'] = self.get_object()
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    models.FamilyInvite.objects.create(from_user=self.request.user, to_user=form.invitee, family=self.get_object())
    return response

class Invites(LoginRequiredMixin, ListView):
  model = models.FamilyInvite
  template_name = 'families/invites.html'

  def get_queryset(self):
    return self.request.user.familyinvite_received.filter(status=0)

class InviteResponse(LoginRequiredMixin,RedirectView):
  url = reverse_lazy('groups:families:invites')

  def get(selg, request, *args, **kwargs):
    invite = get_object_or_404(
      models.FamilyInvite,
      to_user = request.user,
      uuid = kwargs.get('code'),
      status = 0
    )
    if kwargs.get('response') == 'accept':
      invite.status = 1
    else:
      invite.status = 2

    invite.save()

    return super().get(request, *args, **kwargs)
