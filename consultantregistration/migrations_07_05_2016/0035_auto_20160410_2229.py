# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0034_auto_20160410_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='consultant',
            field=models.OneToOneField(to='roles.Profile', related_name='consultantcourse', verbose_name='Consultant'),
        ),
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='course_rep',
            field=models.ForeignKey(to='coursesearch.Course', verbose_name='Course Representative', related_name='courserep'),
        ),
    ]
