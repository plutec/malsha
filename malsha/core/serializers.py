from django.contrib.auth.models import User
from models import Incident, Indicator, Tag
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        for choice in self._choices:
            if choice[0] == obj:
                return choice[1]
        return None
        #return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)

class IndicatorSerializer(serializers.ModelSerializer):
    indicator_type = ChoicesField(choices=Indicator.INDICATOR_CHOICES)
    class Meta:
        model = Indicator
        fields = ('indicator_type', 'value')

class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    #tags = TagSerializer(read_only=True, many=True)
    tags = serializers.StringRelatedField(many=True)
    indicators = IndicatorSerializer(read_only=True, many=True)

    class Meta:
        model = Incident
        fields = ('name', 'tags', 'indicators')
