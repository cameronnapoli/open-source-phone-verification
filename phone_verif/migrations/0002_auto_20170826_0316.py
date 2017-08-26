# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('phone_verif', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationrequestentry',
            name='phone_number',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verificationrequestentry',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='verificationrequestentry',
            name='verification_code',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
