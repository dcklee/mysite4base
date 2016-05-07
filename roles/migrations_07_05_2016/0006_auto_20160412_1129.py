# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0005_auto_20160412_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='courses',
            field=models.ManyToManyField(to='coursesearch.Course', blank=True),
        ),
    ]
