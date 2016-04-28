# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0002_auto_20151119_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='areaofstudy',
            name='fontlogo',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
