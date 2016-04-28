# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0005_educationinstitute_country'),
        ('consultantregistration', '0030_auto_20160410_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseconsultantrelationship',
            name='course_rep',
        ),
        migrations.AddField(
            model_name='courseconsultantrelationship',
            name='course_rep',
            field=models.ForeignKey(verbose_name='Course Representative', default='1', to='coursesearch.Course', related_name='courserep'),
            preserve_default=False,
        ),
    ]
