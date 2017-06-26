# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Incident(models.Model):
    TLP_CHOICES = (
        ('1', 'Red'),
        ('2', 'Amber'),
        ('3', 'Green'),
        ('4', 'White'),
        )
    ATTACK_CHOICES = (
        ('1', 'Other'),
        ('2', 'Malware'),
        ('3', 'Phishing'),
        ('4', 'Fraud'),
    )
    """
    RED
    Developer may permit access to view Threat Data it receives that is labeled with share level RED solely to those employees of Developer who have a strict need to know for the Purpose. Threat Data labeled with share level RED must not be reproduced, retransmitted, or otherwise re-distributed within Developer's organization or to any other party, including but not limited to Developer's affiliates, customers, partners or any other party, in each case, without the prior written consent of the original publisher.
    AMBER
    Developer may share Threat Data it receives that is labeled with share level AMBER solely to Developer and its subsidiaries who have a need to know for the Purpose (as that term is defined in the ThreatExchange Program Terms & Conditions), and solely as widely within Developer's organization(s) as is reasonably necessary for Developer to act on that information.
    GREEN
    Developer may share Threat Data it receives that is labeled with share level GREEN via a non-publicly accessible channel, solely to Developer's peer and partner organizations, preferred vendors, customers, and/or other entities who would find it useful as part of their existing business relationship with Developer, provided in each instance that the third party with whom Developer shares Threat Data has agreed in writing to keep all Threat Data confidential and not disclose Threat Data to any third party.
    WHITE
    Developer may share Threat Data it receives that is labeled with share level WHITE without restriction, subject to any attribution requirements specified by the original publisher(s).
    """

    author = models.ForeignKey(AUTH_USER_MODEL)
    name = models.CharField(max_length=30, null=True, blank=True)
    #last_name = models.CharField(max_length=30)
    tlp = models.CharField(max_length=1, choices=TLP_CHOICES, default=1)
    attack = models.CharField(max_length=1, choices=ATTACK_CHOICES)
    tags = models.ManyToManyField(Tag, blank=True)


class Indicator(models.Model):
    INDICATOR_CHOICES = (
        ('1', 'sha256'),
        ('2', 'sha1'),
        ('3', 'md5'),
        ('4', 'URL'),
        ('5', 'domain'),
        ('6', 'registry'),
        ('7', 'file'),
        ('8', 'source'),
        ('9', 'free text'),
        )

    incident = models.ForeignKey(Incident)
    indicator_type = models.CharField(max_length=2, choices=INDICATOR_CHOICES)
    value = models.CharField(max_length=2048)
    

