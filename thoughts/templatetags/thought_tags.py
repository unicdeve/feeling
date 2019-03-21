from django import template
from django.utils import timezone
import datetime
import json

from ..forms import ThoughtForm

register = template.Library()

@register.inclusion_tag('thoughts/_form.html')
def thought_form():
  form = ThoughtForm
  return {'form': form}

@register.simple_tag(takes_context=True)
def chart_data(context):
  user = context['user']
  ten_days_ago = timezone.now() - datetime.timedelta(days=10)
  thoughts =  user.thoughts.filter(recorder_at__gte=ten_days_ago).order_by('recorder_at')
  return json.dumps({
    'labels': [
      thought.recorder_at.strftime('%Y-%m-%d') for thought in thoughts
    ],
    'series': [[
      thought.conditions*-1 for thought in thoughts
    ]]
  })