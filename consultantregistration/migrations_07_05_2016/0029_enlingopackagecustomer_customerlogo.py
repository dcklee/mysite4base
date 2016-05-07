# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0028_enlingopackagecustomer_schemeregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='customerlogo',
            field=models.ImageField(null=True, upload_to='customerlogo/'),
        ),
    ]
