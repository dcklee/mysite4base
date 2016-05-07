# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0010_auto_20151120_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='consultant_1',
            field=models.ForeignKey(to='roles.Profile', related_query_name='consultantcourse', verbose_name='Consultant'),
        ),
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='course_rep',
            field=models.ManyToManyField(to='coursesearch.Course', related_query_name='courserep', verbose_name='Course Representative'),
        ),
    ]
