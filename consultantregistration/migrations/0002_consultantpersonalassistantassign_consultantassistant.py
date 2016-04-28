# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('consultantregistration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantpersonalassistantassign',
            name='consultantassistant',
            field=models.ForeignKey(to='roles.Profile', default=1, related_name='ConsultantAssistant'),
            preserve_default=False,
        ),
    ]
