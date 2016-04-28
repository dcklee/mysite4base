# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberpackage', '0005_auto_20160406_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlingocreditrecharge',
            name='currency',
            field=models.CharField(default='AUD', choices=[('AUD', 'Australian Dollar'), ('CNY', 'Renminbi'), ('USD', 'US Dollar'), ('EUR', 'Euro'), ('GBP', 'Pound Sterling'), ('HKD', 'HK Dollar'), ('SGD', 'Singapore Dollar')], max_length=3),
            preserve_default=False,
        ),
    ]
