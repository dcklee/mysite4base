# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0013_auto_20160411_1404'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseconsultantrelationship',
            unique_together=set([('consultant', 'course_rep')]),
        ),
    ]
