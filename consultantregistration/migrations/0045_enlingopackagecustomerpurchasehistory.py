# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0044_enlingopackagecustomer_education_institute'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlingoPackageCustomerPurchaseHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('item', models.CharField(verbose_name='Item', max_length=50)),
                ('billing_name', models.CharField(verbose_name='Name', max_length=20)),
                ('billing_address_country', models.CharField(verbose_name='Country', max_length=20)),
                ('billing_address_zip', models.CharField(verbose_name='Zip', max_length=10)),
                ('billing_address_state', models.CharField(verbose_name='State', max_length=20)),
                ('billing_address_line1', models.CharField(verbose_name='Address Line 1', max_length=50)),
                ('billing_address_city', models.CharField(verbose_name='City', max_length=20)),
                ('group', models.ForeignKey(null=True, to='consultantregistration.EnlingoPackageCustomer')),
            ],
            options={
                'verbose_name': 'Enlingo Package Customer Purchase History',
            },
        ),
    ]
