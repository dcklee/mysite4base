# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberpackage', '0004_auto_20160405_1802'),
        ('consultantregistration', '0013_enlingopackageadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='rechargehistory',
        ),
        migrations.AddField(
            model_name='enlingopackageadmin',
            name='rechargehistory',
            field=models.ManyToManyField(to='memberpackage.EnlingoCreditRecharge'),
        ),
    ]
