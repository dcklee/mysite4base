# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberpackage', '0005_auto_20160406_1431'),
        ('consultantregistration', '0023_auto_20160406_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlingoPackageAdminGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('groupname', models.CharField(max_length=20, null=True, verbose_name='Group Name')),
                ('autorecharge', models.BooleanField()),
                ('creditbalance', models.IntegerField(null=True)),
                ('rechargeindicator', models.IntegerField(null=True)),
                ('credits', models.IntegerField(null=True)),
                ('debits', models.IntegerField(null=True)),
                ('packadmin', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(to='memberpackage.EnlingoPackage', null=True)),
            ],
            options={
                'verbose_name': 'Enlingo Package Member Group',
                'verbose_name_plural': 'Enlingo Package Member Groups',
            },
        ),
        migrations.CreateModel(
            name='EnlingoPackageAdminGroupBillingDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('billing_name', models.CharField(max_length=20, verbose_name='Name')),
                ('billing_address_country', models.CharField(max_length=20, verbose_name='Country')),
                ('billing_address_zip', models.CharField(max_length=10, verbose_name='Zip')),
                ('billing_address_state', models.CharField(max_length=20, verbose_name='State')),
                ('billing_address_line1', models.CharField(max_length=20, verbose_name='Address Line 1')),
                ('billing_address_city', models.CharField(max_length=20, verbose_name='City')),
                ('group', models.OneToOneField(to='consultantregistration.EnlingoPackageAdminGroup', null=True)),
            ],
            options={
                'verbose_name': 'Enlingo Package Member Group Billing Details',
                'verbose_name_plural': 'Enlingo Package Member Group Billing Details',
            },
        ),
        migrations.CreateModel(
            name='EnlingoPackageMember',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('member', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('membergroupadmin', models.ForeignKey(to='consultantregistration.EnlingoPackageAdminGroup', null=True)),
            ],
            options={
                'verbose_name': 'Enlingo Package Member',
                'verbose_name_plural': 'Enlingo Package Members',
            },
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='packadmin',
        ),
        migrations.RemoveField(
            model_name='enlingopackageadmin',
            name='package',
        ),
        migrations.RemoveField(
            model_name='consultantregistrationdetails',
            name='prior_work_experience',
        ),
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='prior_work_company_name',
            field=models.CharField(verbose_name='Prior Workplace Name', max_length=20, default='HL Priming Pty Ltd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='prior_work_position',
            field=models.CharField(verbose_name='Prior Work Position', max_length=30, default='General Manager'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='academic_qualifications',
            field=models.CharField(max_length=50, verbose_name='Academic Qualifications'),
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='cities_lived_worked_in',
            field=models.CharField(max_length=20, verbose_name='Cities worked or lived in'),
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='location',
            field=models.CharField(max_length=20, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='registration_qualifications',
            field=models.CharField(max_length=50, verbose_name='Professional Qualifications'),
        ),
        migrations.DeleteModel(
            name='EnlingoPackageAdmin',
        ),
    ]
