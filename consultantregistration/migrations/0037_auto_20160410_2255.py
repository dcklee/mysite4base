# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0036_auto_20160410_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultantpersonalassistantassign',
            old_name='consultant_2',
            new_name='consultant',
        ),
    ]
