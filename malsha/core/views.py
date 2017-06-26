# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from models import Incident, Indicator
from rest_framework import viewsets
from serializers import IncidentSerializer, IndicatorSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Incident.objects.all()#.order_by('-date_joined')
    serializer_class = IncidentSerializer


class IndicatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer