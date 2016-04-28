# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0045_enlingopackagecustomerpurchasehistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enlingopackagecustomerpurchasehistory',
            name='group',
        ),
        migrations.DeleteModel(
            name='EnlingoPackageCustomerPurchaseHistory',
        ),
    ]
