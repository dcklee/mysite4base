# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import localflavor.au.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=4, choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr')], null=True)),
                ('dateofbirth', models.DateField(null=True)),
                ('sex', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neuter')], null=True)),
                ('phone', models.CharField(max_length=15, verbose_name='phone', null=True)),
                ('address_1', models.CharField(max_length=128, verbose_name='address', null=True)),
                ('address_2', models.CharField(max_length=128, verbose_name="address cont'd", null=True)),
                ('city', models.CharField(max_length=64, verbose_name='city', null=True)),
                ('state', localflavor.au.models.AUStateField(max_length=3, choices=[('ACT', 'Australian Capital Territory'), ('NSW', 'New South Wales'), ('NT', 'Northern Territory'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('TAS', 'Tasmania'), ('VIC', 'Victoria'), ('WA', 'Western Australia')], verbose_name='state', null=True)),
                ('postcode', localflavor.au.models.AUPostCodeField(max_length=4, verbose_name='postcode', null=True)),
                ('urole', models.CharField(max_length=20, choices=[('S', 'Student'), ('C', 'Consultant'), ('CA', 'Consultant Assistant')], verbose_name='User Role', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
