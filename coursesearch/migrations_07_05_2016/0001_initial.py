# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfStudy',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=200, verbose_name='Course ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_type', models.CharField(max_length=30, choices=[('AD', 'Associate Degree'), ('D', 'Diploma'), ('GD', 'Graduate Diploma'), ('B', 'Bachelors'), ('M', 'Masters'), ('P', 'PHD')])),
                ('course_cricos_id', models.CharField(max_length=200, verbose_name='CRICOS ID')),
                ('course_semester', models.CharField(max_length=50, verbose_name='Course semester')),
                ('course_start_date', models.DateField(verbose_name='Course start date')),
                ('application_deadline', models.DateField(verbose_name='Course deadline date')),
                ('faculty_name', models.CharField(max_length=50, verbose_name='Faculty')),
                ('areaofstudy', models.ManyToManyField(to='coursesearch.AreaOfStudy')),
            ],
        ),
        migrations.CreateModel(
            name='EducationInstitute',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('provider_number', models.CharField(max_length=15, verbose_name='Provider Number')),
                ('website', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('campus', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='educationalinstitution',
            field=models.ForeignKey(to='coursesearch.EducationInstitute'),
        ),
    ]
