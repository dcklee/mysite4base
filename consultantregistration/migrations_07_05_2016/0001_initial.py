# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('coursesearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultantPersonalAssistantAssign',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('consultant_2', models.OneToOneField(to='roles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultantRegistrationDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('registration_qualifications', models.TextField(verbose_name='Professional Qualifications')),
                ('academic_qualifications', models.TextField(verbose_name='Academic Qualifications')),
                ('prior_work_experience', models.TextField(verbose_name='Prior Work Experience')),
                ('cities_lived_worked_in', models.TextField(verbose_name='Cities worked or lived in')),
                ('consultant_3', models.OneToOneField(to='roles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CourseConsultantRelationship',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('outlook_statement', models.TextField(verbose_name='Course Outlook')),
                ('consultant_1', models.OneToOneField(to='roles.Profile')),
                ('course_rep', models.ManyToManyField(to='coursesearch.Course')),
            ],
        ),
    ]
