# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberpackage', '0004_auto_20160405_1802'),
        ('consultantregistration', '0019_auto_20160405_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlingoPackageAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('autorecharge', models.BooleanField()),
                ('creditbalance', models.IntegerField()),
                ('rechargeindicator', models.IntegerField()),
                ('credits', models.IntegerField()),
                ('debits', models.IntegerField()),
                ('packadmin', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(to='memberpackage.EnlingoPackage')),
            ],
            options={
                'verbose_name': 'Enlingo Package Member Administrator',
                'verbose_name_plural': 'Enlingo Package Member Administrators',
            },
        ),
    ]
