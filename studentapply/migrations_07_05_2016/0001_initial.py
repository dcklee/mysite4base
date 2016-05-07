# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0002_fsmchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='viewflow.Process')),
                ('text', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
        migrations.CreateModel(
            name='StudentApply',
            fields=[
                ('process_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='viewflow.Process')),
                ('text', models.CharField(max_length=150, verbose_name='Course ID')),
                ('approved', models.BooleanField(default=False, verbose_name='Successful Submit')),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
