# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0004_profile_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='courses',
            field=models.ManyToManyField(null=True, to='coursesearch.Course'),
        ),
    ]
