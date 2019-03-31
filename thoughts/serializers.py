from rest_framework import serializers

from . import models


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Thought
    fields = ('recorder_at', 'conditions', 'notes')
    read_only_fields = ('recorder_at',)

  def create(self, validated_data):
    thought = models.Thought(**validated_data)
    thought.user = self.context['request'].user
    thought.save()
    return thought
