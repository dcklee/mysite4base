# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.au.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coursesearch', '0004_educationinstitute_country'),
        ('memberpackage', '0005_auto_20160406_1431'),
        ('consultantregistration', '0012_auto_20151121_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlingoPackageCustomer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('customername', models.CharField(null=True, max_length=50, verbose_name='Customer Name')),
                ('customerlogo', models.ImageField(null=True, upload_to='customerlogo/')),
                ('website', models.CharField(null=True, max_length=50, verbose_name='Web Site')),
                ('phone', models.CharField(null=True, max_length=15, verbose_name='phone')),
                ('address_1', models.CharField(null=True, max_length=50, verbose_name='address')),
                ('address_2', models.CharField(null=True, max_length=50, verbose_name="address cont'd")),
                ('city', models.CharField(null=True, max_length=50, verbose_name='city')),
                ('state', localflavor.au.models.AUStateField(choices=[('ACT', 'Australian Capital Territory'), ('NSW', 'New South Wales'), ('NT', 'Northern Territory'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('TAS', 'Tasmania'), ('VIC', 'Victoria'), ('WA', 'Western Australia')], null=True, max_length=3, verbose_name='state')),
                ('postcode', localflavor.au.models.AUPostCodeField(null=True, max_length=4, verbose_name='postcode')),
                ('autorecharge', models.BooleanField()),
                ('schemeregister', models.BooleanField()),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
        migrations.CreateModel(
            name='EnlingoPackageMember',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('customer_account', models.ForeignKey(null=True, to='consultantregistration.EnlingoPackageCustomer')),
                ('member', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Enlingo Package Member',
                'verbose_name_plural': 'Enlingo Package Members',
            },
        ),
        migrations.AlterModelOptions(
            name='consultantpersonalassistantassign',
            options={'verbose_name': 'Enlingo Package Member Member Manager', 'verbose_name_plural': 'Enlingo Package Member Member Managers'},
        ),
        migrations.AlterModelOptions(
            name='consultantregistrationdetails',
            options={'verbose_name': 'Enlingo Member Profile Details', 'verbose_name_plural': 'Enlingo Member Profile Details'},
        ),
        migrations.AlterModelOptions(
            name='courseconsultantrelationship',
            options={'verbose_name': 'Enlingo Member Course Service Professional', 'verbose_name_plural': 'Enlingo Member Course Service Professionals'},
        ),
        migrations.RenameField(
            model_name='consultantpersonalassistantassign',
            old_name='consultant_2',
            new_name='consultant',
        ),
        migrations.RenameField(
            model_name='consultantregistrationdetails',
            old_name='consultant_3',
            new_name='consultant',
        ),
        migrations.RenameField(
            model_name='courseconsultantrelationship',
            old_name='consultant_1',
            new_name='consultant',
        ),
        migrations.RemoveField(
            model_name='consultantregistrationdetails',
            name='prior_work_experience',
        ),
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='position',
            field=models.CharField(default='Director', verbose_name='Position', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='prior_work_company_name',
            field=models.CharField(default='Enlingo', verbose_name='Prior Workplace Name', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='prior_work_position',
            field=models.CharField(default='General Manager', verbose_name='Prior Work Position', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='academic_qualifications',
            field=models.CharField(verbose_name='Academic Qualifications', max_length=50),
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='cities_lived_worked_in',
            field=models.CharField(verbose_name='Cities worked or lived in', max_length=20),
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='location',
            field=models.CharField(verbose_name='Location', max_length=20),
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='registration_qualifications',
            field=models.CharField(verbose_name='Professional Qualifications', max_length=50),
        ),
        migrations.RemoveField(
            model_name='courseconsultantrelationship',
            name='course_rep',
        ),
        migrations.AddField(
            model_name='courseconsultantrelationship',
            name='course_rep',
            field=models.ForeignKey(to='coursesearch.Course', related_name='courserep', default=1, verbose_name='Course Representative'),
            preserve_default=False,
        ),
    ]
