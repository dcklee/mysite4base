# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0002_consultantpersonalassistantassign_consultantassistant'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantpersonalassistantassign',
            name='binding',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
