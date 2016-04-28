# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0024_auto_20160406_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enlingopackageadmingroup',
            name='groupname',
            field=models.CharField(verbose_name='Group Name', null=True, max_length=50),
        ),
    ]
