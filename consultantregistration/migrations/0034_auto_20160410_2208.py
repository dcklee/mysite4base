# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0033_auto_20160410_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='consultant',
            field=models.ForeignKey(to='roles.Profile', related_name='consultantcourse', verbose_name='Consultant'),
        ),
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='course_rep',
            field=models.OneToOneField(to='coursesearch.Course', related_name='courserep', verbose_name='Course Representative'),
        ),
    ]
