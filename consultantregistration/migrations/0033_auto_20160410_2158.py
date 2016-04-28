# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0032_auto_20160410_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='consultant',
            field=models.OneToOneField(to='roles.Profile', verbose_name='Consultant', related_name='consultantcourse'),
        ),
    ]
