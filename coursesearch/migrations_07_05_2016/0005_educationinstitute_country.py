# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0004_auto_20151203_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationinstitute',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, default='US'),
            preserve_default=False,
        ),
    ]
