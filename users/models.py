
"""User model"""

#django
from django.db import models
from django.core.validators import RegexValidator

from utils.models import CommonFields

class User(CommonFields):
    """User Model"""
    company = models.CharField(max_length=30)

    full_name = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'The email should be unique'
        }
    )

    job = models.CharField(max_length=30)

    amount_users = models.IntegerField()

    country = models.CharField(
        max_length=35,
        blank=True,
        null=True
    )

    cp = models.CharField(max_length=5)

    state = models.CharField(max_length=30)

    address = models.TextField()

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{10}',
        message='El formato del número debe ser 9999999999'
    )

    phone_number = models.CharField(
        max_length=10,
        blank=True,
        validators=[phone_regex]
    )
    password_regex = RegexValidator(
        regex='^[A-Za-z0-9@#$]{8,16}$',
        message='Password doesnt comply'
    )

    password = models.CharField(
        max_length=256,
        validators=[password_regex]
    )

    def __str__(self):
        return self.full_name