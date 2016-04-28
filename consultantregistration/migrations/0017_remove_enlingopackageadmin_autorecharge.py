# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0016_auto_20160405_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='autorecharge',
        ),
    ]
