# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0004_educationinstitute_country'),
        ('consultantregistration', '0014_auto_20160412_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='association',
            field=models.CharField(default='Migration Alliance', verbose_name='Membership Association', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='education_institute',
            field=models.ManyToManyField(blank=True, to='coursesearch.EducationInstitute'),
        ),
        migrations.AlterField(
            model_name='enlingopackagecustomer',
            name='packadmin',
            field=models.OneToOneField(to='roles.Profile'),
        ),
        migrations.AlterField(
            model_name='enlingopackagemember',
            name='member',
            field=models.OneToOneField(to='roles.Profile'),
        ),
    ]
