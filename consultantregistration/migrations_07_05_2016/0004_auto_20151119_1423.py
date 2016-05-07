# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0003_consultantpersonalassistantassign_binding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultantpersonalassistantassign',
            name='binding',
        ),
        migrations.AddField(
            model_name='consultantpersonalassistantassign',
            name='reason',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultantpersonalassistantassign',
            name='consultant_2',
            field=models.ForeignKey(to='roles.Profile', related_name='Consultant'),
        ),
    ]
