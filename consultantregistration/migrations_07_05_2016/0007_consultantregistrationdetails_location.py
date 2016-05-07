# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0006_auto_20151119_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='location',
            field=models.TextField(verbose_name='Location', default=1),
            preserve_default=False,
        ),
    ]
