# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0007_consultantregistrationdetails_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantpersonalassistantassign',
            name='consultantassistant',
            field=models.OneToOneField(related_name='ConsultantAssistant', to='roles.Profile', verbose_name='Consultant Assistant'),
        ),
    ]
