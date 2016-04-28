# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0004_auto_20151119_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantpersonalassistantassign',
            name='consultant_2',
            field=models.ForeignKey(verbose_name='Consultant', to='roles.Profile', related_name='Consultant'),
        ),
        migrations.AlterField(
            model_name='consultantpersonalassistantassign',
            name='consultantassistant',
            field=models.ForeignKey(verbose_name='Consultant Assistant', to='roles.Profile', related_name='ConsultantAssistant'),
        ),
        migrations.AlterField(
            model_name='consultantregistrationdetails',
            name='consultant_3',
            field=models.OneToOneField(verbose_name='Consultant', to='roles.Profile'),
        ),
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='consultant_1',
            field=models.OneToOneField(verbose_name='Consultant', to='roles.Profile'),
        ),
        migrations.AlterField(
            model_name='courseconsultantrelationship',
            name='course_rep',
            field=models.ManyToManyField(verbose_name='Course Representative', to='coursesearch.Course'),
        ),
    ]
