# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberpackage', '0003_remove_enlingocreditrecharge_rechargeaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credits',
            name='creditaccount',
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='packadmin',
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='package',
        ),
        migrations.DeleteModel(
            name='Credits',
        ),
        migrations.DeleteModel(
            name='EnlingoPackageAdmin',
        ),
    ]
