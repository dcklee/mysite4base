# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0006_auto_20160412_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='courses',
        ),
    ]
