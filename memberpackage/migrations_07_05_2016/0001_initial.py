# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('rechargeindicator', models.IntegerField()),
                ('credits', models.IntegerField()),
                ('debits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CreditValue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creditvalue', models.IntegerField()),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='EnlingoCreditRecharge',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('rechargeid', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnlingoPackage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('packageid', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('credits', models.IntegerField()),
                ('useraccountlimit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnlingoPackageAdmin',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('packadmin', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('package', models.OneToOneField(to='memberpackage.EnlingoPackage')),
            ],
        ),
        migrations.AddField(
            model_name='enlingocreditrecharge',
            name='rechargeaccount',
            field=models.ForeignKey(to='memberpackage.EnlingoPackageAdmin'),
        ),
        migrations.AddField(
            model_name='creditvalue',
            name='creditaccount',
            field=models.OneToOneField(to='memberpackage.EnlingoPackage'),
        ),
        migrations.AddField(
            model_name='credits',
            name='creditaccount',
            field=models.OneToOneField(to='memberpackage.EnlingoPackageAdmin'),
        ),
    ]
