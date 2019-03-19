from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

CONDITIONS = (
    (0, 'Ecstatic'),
    (5, 'Passionate'),
    (10, 'Happy'),
    (15, 'Optimistic'),
    (20, 'Content'),
    (25, 'Bored'),
    (26, 'Tired'),
    (27, 'Hungry'),
    (30, 'Pessimistic'),
    (35, 'Frustrated'),
    (40, 'Overwhelmed'),
    (45, 'Disappointed'),
    (50, 'Worried'),
    (55, 'Angry'),
    (60, 'Jealous'),
    (65, 'Insecure'),
    (70, 'Guilty'),
    (75, 'Fear'),
    (80, 'Grief'),
    (85, 'Despair'),
    (90, 'Paranoid'),
)

# Create your models here.
class Thought(models.Model):
    user = models.ForeignKey(User, related_name='thoughts')
    recorder_at = models.DateTimeField(default=timezone.now, editable=False)
    conditions = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return '{}: {}'.format(self.recorder_at.strftime("%Y-%m-%d %H:%M"), self.get_conditions_display())