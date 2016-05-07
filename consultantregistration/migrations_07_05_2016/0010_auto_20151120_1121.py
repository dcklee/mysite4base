# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0009_auto_20151120_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='consultant_1',
            field=models.ForeignKey(to='roles.Profile', verbose_name='Consultant'),
        ),
    ]
