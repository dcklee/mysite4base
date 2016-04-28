# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0027_auto_20160409_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='schemeregister',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
