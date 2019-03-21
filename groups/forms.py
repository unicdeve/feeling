from . import models
from django import forms

class FamilyForm(forms.ModelForm):
  class Meta:
    fields = ('name', 'description')
    model = models.Family


class CompanyForm(forms.ModelForm):
  class Meta:
    fields = ('name', 'description')
    model = models.Company