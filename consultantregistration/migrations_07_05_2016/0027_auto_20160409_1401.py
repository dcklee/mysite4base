# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberpackage', '0005_auto_20160406_1431'),
        ('consultantregistration', '0026_auto_20160406_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlingoPackageCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('customername', models.CharField(verbose_name='Customer Name', null=True, max_length=50)),
                ('autorecharge', models.BooleanField()),
                ('creditbalance', models.IntegerField(null=True)),
                ('rechargeindicator', models.IntegerField(null=True)),
                ('credits', models.IntegerField(null=True)),
                ('debits', models.IntegerField(null=True)),
                ('packadmin', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(null=True, to='memberpackage.EnlingoPackage')),
            ],
            options={
                'verbose_name': 'Enlingo Package Customer',
                'verbose_name_plural': 'Enlingo Package Customers',
            },
        ),
        migrations.CreateModel(
            name='EnlingoPackageCustomerBillingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('billing_name', models.CharField(verbose_name='Name', max_length=20)),
                ('billing_address_country', models.CharField(verbose_name='Country', max_length=20)),
                ('billing_address_zip', models.CharField(verbose_name='Zip', max_length=10)),
                ('billing_address_state', models.CharField(verbose_name='State', max_length=20)),
                ('billing_address_line1', models.CharField(verbose_name='Address Line 1', max_length=50)),
                ('billing_address_city', models.CharField(verbose_name='City', max_length=20)),
                ('group', models.OneToOneField(null=True, to='consultantregistration.EnlingoPackageCustomer')),
            ],
            options={
                'verbose_name': 'Enlingo Package Customer Billing Details',
                'verbose_name_plural': 'Enlingo Package Customer Billing Details',
            },
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmingroup',
            name='packadmin',
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmingroup',
            name='package',
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmingroupbillingdetails',
            name='group',
        ),
        migrations.AlterField(
            model_name='enlingopackagemember',
            name='membergroupadmin',
            field=models.ForeignKey(null=True, to='consultantregistration.EnlingoPackageCustomer'),
        ),
        migrations.DeleteModel(
            name='EnlingoPackageAdminGroup',
        ),
        migrations.DeleteModel(
            name='EnlingoPackageAdminGroupBillingDetails',
        ),
    ]
