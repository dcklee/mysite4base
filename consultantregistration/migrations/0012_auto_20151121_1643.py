# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0011_auto_20151120_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='consultant_1',
            field=models.ForeignKey(verbose_name='Consultant', to='roles.Profile', related_name='consultantcourse'),
        ),
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='course_rep',
            field=models.ManyToManyField(verbose_name='Course Representative', related_name='courserep', to='coursesearch.Course'),
        ),
    ]
