# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberpackage', '0002_auto_20160405_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enlingocreditrecharge',
            name='rechargeaccount',
        ),
    ]
