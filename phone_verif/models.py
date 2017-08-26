from django.db import models
from django.contrib.auth.models import User


class VerificationRequestEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=200)
    verification_code = models.CharField(max_length=200)
