# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_verif', '0002_auto_20170826_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verificationrequestentry',
            name='user',
        ),
        migrations.DeleteModel(
            name='VerificationRequestEntry',
        ),
    ]
