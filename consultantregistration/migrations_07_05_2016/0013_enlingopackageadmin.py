# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberpackage', '0004_auto_20160405_1802'),
        ('consultantregistration', '0012_auto_20151121_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlingoPackageAdmin',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creditbalance', models.IntegerField()),
                ('rechargeindicator', models.IntegerField()),
                ('autorecharge', models.CharField(max_length=20)),
                ('credits', models.IntegerField()),
                ('debits', models.IntegerField()),
                ('packadmin', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(to='memberpackage.EnlingoPackage')),
                ('rechargehistory', models.ForeignKey(to='memberpackage.EnlingoCreditRecharge')),
            ],
        ),
    ]
