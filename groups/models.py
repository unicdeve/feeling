from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from autoslug import AutoSlugField

class Group(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  created_by = models.ForeignKey(User, related_name='%(class)s_created')
  name = models.CharField(max_length=200)
  slug = AutoSlugField(populate_from='name')
  description = models.TextField(default='')

  class Meta:
    abstract = True

class Family(Group):
  members = models.ManyToManyField(User, related_name='families')

  class Meta:
    verbose_name_plural = 'families'

class Company(Group):
  members = models.ManyToManyField(User, related_name='companies')

  class Meta:
    verbose_name_plural = 'companies'

  def __str__(self):
    return self.name
