# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0037_auto_20160410_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultantregistrationdetails',
            old_name='consultant_3',
            new_name='consultant',
        ),
    ]
