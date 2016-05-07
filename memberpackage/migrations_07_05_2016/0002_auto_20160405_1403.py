# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberpackage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditvalue',
            name='creditvalue',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='enlingocreditrecharge',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='enlingopackage',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
