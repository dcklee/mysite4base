# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0014_auto_20160405_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='rechargehistory',
        ),
    ]
