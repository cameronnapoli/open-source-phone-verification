"""
models.py
Written by: Cameron Napoli
"""

from django.db import models
from django.contrib.auth.models import User


class UserVerified(models.Model):
    ''' One-to-one table which will hold data on
        whether a user is verified or not. '''
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User Verified'
        verbose_name_plural = 'User Verified'


class VerificationRequestEntry(models.Model):
    ''' DB to hold data for phone number, verification code,
        and User. '''
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    phone_number = models.CharField(max_length=200)
    verification_code = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Verification Request Entry'
        verbose_name_plural = 'Verification Request Entries'
