# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultantregistration', '0031_auto_20160410_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultantpersonalassistantassign',
            options={'verbose_name': 'Enlingo Package Member Member Manager', 'verbose_name_plural': 'Enlingo Package Member Member Managers'},
        ),
        migrations.AlterModelOptions(
            name='consultantregistrationdetails',
            options={'verbose_name': 'Enlingo Member Profile Details', 'verbose_name_plural': 'Enlingo Member Profile Details'},
        ),
        migrations.AlterModelOptions(
            name='courseconsultantrelationship',
            options={'verbose_name': 'Enlingo Member Course Service Professional', 'verbose_name_plural': 'Enlingo Member Course Service Professionals'},
        ),
        migrations.RenameField(
            model_name='courseconsultantrelationship',
            old_name='consultant_1',
            new_name='consultant',
        ),
    ]
