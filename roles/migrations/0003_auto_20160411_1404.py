# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_1',
            field=models.CharField(null=True, max_length=50, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_2',
            field=models.CharField(null=True, max_length=50, verbose_name="address cont'd"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(null=True, max_length=50, verbose_name='city'),
        ),
    ]
