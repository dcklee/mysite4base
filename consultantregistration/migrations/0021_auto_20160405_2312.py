# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0020_enlingopackageadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enlingopackageadmin',
            name='autorecharge',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='enlingopackageadmin',
            name='creditbalance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enlingopackageadmin',
            name='credits',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enlingopackageadmin',
            name='debits',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enlingopackageadmin',
            name='rechargeindicator',
            field=models.IntegerField(null=True),
        ),
    ]
