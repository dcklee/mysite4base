# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0005_auto_20151119_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantpersonalassistantassign',
            name='reason',
            field=models.CharField(null=True, max_length=20, verbose_name='Referral Source'),
        ),
    ]
