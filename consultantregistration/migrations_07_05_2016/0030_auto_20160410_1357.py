# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0029_enlingopackagecustomer_customerlogo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enlingopackagemember',
            old_name='membergroupadmin',
            new_name='customer_account',
        ),
    ]
