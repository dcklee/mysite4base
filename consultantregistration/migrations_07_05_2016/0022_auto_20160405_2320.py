# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0021_auto_20160405_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enlingopackageadmin',
            name='package',
            field=models.ForeignKey(null=True, to='memberpackage.EnlingoPackage'),
        ),
    ]
