# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import random

# Model states
MODEL_STATES = {
    'ACTIVE': '1',
    'DELETE': '-1'
}

STATES = [
    (MODEL_STATES['DELETE'], 'Inactivo'),
    (MODEL_STATES['ACTIVE'], 'Activo'),
]


class Apimodel(models.Model):
    ACTIVE = MODEL_STATES['ACTIVE']
    DELETE = MODEL_STATES['DELETE']
    STATES = [
        (DELETE, 'Inactivo'),
        (ACTIVE, 'Activo'),
    ]
    estado = models.CharField(
        max_length=10,
        choices=STATES,
        default=ACTIVE
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    last_modified = models.DateTimeField(
        null=True,
        auto_now=True
    )

    class Meta:
        abstract = True


class INaturalistSettings(Apimodel):
    auth_code = models.TextField()
    token = models.TextField()
    created = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
