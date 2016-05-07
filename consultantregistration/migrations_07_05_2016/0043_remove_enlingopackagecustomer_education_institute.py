# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0042_auto_20160412_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enlingopackagecustomer',
            name='education_institute',
        ),
    ]
