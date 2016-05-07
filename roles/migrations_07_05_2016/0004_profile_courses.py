# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0005_educationinstitute_country'),
        ('roles', '0003_auto_20160411_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='courses',
            field=models.ManyToManyField(to='coursesearch.Course'),
        ),
    ]
