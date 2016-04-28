# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0017_remove_enlingopackageadmin_autorecharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlingopackageadmin',
            name='autorecharge',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
