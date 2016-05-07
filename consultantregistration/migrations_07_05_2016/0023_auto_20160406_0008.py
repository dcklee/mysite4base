# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0022_auto_20160405_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enlingopackageadmin',
            name='autorecharge',
            field=models.BooleanField(),
        ),
    ]
