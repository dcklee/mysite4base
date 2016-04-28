# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0008_auto_20151120_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantpersonalassistantassign',
            name='consultant_2',
            field=models.OneToOneField(verbose_name='Consultant', to='roles.Profile', related_name='Consultant'),
        ),
        migrations.AlterField(
            model_name='consultantpersonalassistantassign',
            name='consultantassistant',
            field=models.ForeignKey(verbose_name='Consultant Assistant', to='roles.Profile', related_name='ConsultantAssistant'),
        ),
    ]
