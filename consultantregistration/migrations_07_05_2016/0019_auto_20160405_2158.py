# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0018_enlingopackageadmin_autorecharge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='packadmin',
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='package',
        ),
        migrations.DeleteModel(
            name='EnlingoPackageAdmin',
        ),
    ]
