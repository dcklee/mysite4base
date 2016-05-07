# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0025_auto_20160406_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enlingopackageadmingroupbillingdetails',
            name='billing_address_line1',
            field=models.CharField(verbose_name='Address Line 1', max_length=50),
        ),
    ]
