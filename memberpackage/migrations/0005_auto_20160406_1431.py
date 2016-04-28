# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberpackage', '0004_auto_20160405_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlingopackage',
            name='currency',
            field=models.CharField(choices=[('AUD', 'Australian Dollar'), ('CNY', 'Renminbi'), ('USD', 'US Dollar'), ('EUR', 'Euro'), ('GBP', 'Pound Sterling'), ('HKD', 'HK Dollar'), ('SGD', 'Singapore Dollar')], max_length=3, default='AUD'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creditvalue',
            name='currency',
            field=models.CharField(choices=[('AUD', 'Australian Dollar'), ('CNY', 'Renminbi'), ('USD', 'US Dollar'), ('EUR', 'Euro'), ('GBP', 'Pound Sterling'), ('HKD', 'HK Dollar'), ('SGD', 'Singapore Dollar')], max_length=3),
        ),
    ]
