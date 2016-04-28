# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0041_auto_20160412_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enlingopackagecustomer',
            name='packadmin',
            field=models.OneToOneField(to='roles.Profile'),
        ),
        migrations.AlterField(
            model_name='enlingopackagemember',
            name='member',
            field=models.OneToOneField(to='roles.Profile'),
        ),
    ]
