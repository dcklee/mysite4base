# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(verbose_name='Duration', max_length=10, default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='fees',
            field=models.CharField(verbose_name='Fees', max_length=10, default=20000),
            preserve_default=False,
        ),
    ]
