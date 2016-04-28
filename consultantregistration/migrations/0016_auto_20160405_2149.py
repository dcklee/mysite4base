# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0015_remove_enlingopackageadmin_rechargehistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enlingopackageadmin',
            options={'verbose_name': 'Enlingo Package Member Administrator', 'verbose_name_plural': 'Enlingo Package Member Administrators'},
        ),
    ]
