# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0005_educationinstitute_country'),
        ('consultantregistration', '0043_remove_enlingopackagecustomer_education_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlingopackagecustomer',
            name='education_institute',
            field=models.ManyToManyField(blank=True, to='coursesearch.EducationInstitute'),
        ),
    ]
