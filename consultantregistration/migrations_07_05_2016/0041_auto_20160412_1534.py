# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0005_educationinstitute_country'),
        ('consultantregistration', '0040_auto_20160412_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantregistrationdetails',
            name='association',
            field=models.CharField(verbose_name='Membership Association', max_length=50, default='Migration Alliance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='education_institute',
            field=models.ManyToManyField(to='coursesearch.EducationInstitute', blank=True),
        ),
    ]
