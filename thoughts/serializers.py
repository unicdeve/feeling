from rest_framework import serializers

from . import models


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
  conditions_display = serializers.SerializerMethodField()

  class Meta:
    model = models.Thought
    fields = ('recorder_at', 'conditions', 'conditions_display', 'notes',
              'user')
    read_only_fields = ('recorder_at',)

  def create(self, validated_data):
    thought = models.Thought(**validated_data)
    thought.user = self.context['request'].user
    thought.save()
    return thought

  def get_conditions_display(self, obj):
    return obj.get_conditions_display()
