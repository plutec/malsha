from django.contrib.auth.models import User
from models import Incident, Indicator
from rest_framework import serializers


class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incident
        fields = ('name', 'tags',)


class IndicatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicator
        fields = ('value')