# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.au.models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0038_auto_20160410_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='position',
            field=models.CharField(default='Director', verbose_name='Position', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='address_1',
            field=models.CharField(verbose_name='address', null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='address_2',
            field=models.CharField(verbose_name="address cont'd", null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='city',
            field=models.CharField(verbose_name='city', null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='phone',
            field=models.CharField(verbose_name='phone', null=True, max_length=15),
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='postcode',
            field=localflavor.au.models.AUPostCodeField(verbose_name='postcode', null=True, max_length=4),
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='state',
            field=localflavor.au.models.AUStateField(choices=[('ACT', 'Australian Capital Territory'), ('NSW', 'New South Wales'), ('NT', 'Northern Territory'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('TAS', 'Tasmania'), ('VIC', 'Victoria'), ('WA', 'Western Australia')], verbose_name='state', null=True, max_length=3),
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='website',
            field=models.CharField(verbose_name='Web Site', null=True, max_length=50),
        ),
    ]
