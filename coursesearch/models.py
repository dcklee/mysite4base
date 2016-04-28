from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class AreaOfStudy(models.Model):
    def __str__(self):
        return self.name
    name =  models.CharField(max_length=200)
    fontlogo = models.CharField(max_length=30)



class EducationInstitute(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    provider_number = models.CharField('Provider Number', max_length=15)
    website = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    campus = models.CharField(max_length=200)
    country = CountryField()


class Course(models.Model):
    def __str__(self):
        return self.course_name
    #course type Items Attributes for "course_type" field: eg bachelor
    ASSOCIATE_DEGREE = 'AD'
    DIPLOMA = "D"
    GRADUATE_DIPLOMA = "GD"
    BACHELORS = 'B'
    MASTERS = 'M'
    PHD = "P"

    CTYPE_CHOICES = ((ASSOCIATE_DEGREE, 'Associate Degree'),
                    (DIPLOMA, 'Diploma'),
                    (GRADUATE_DIPLOMA, 'Graduate Diploma'),
                    (BACHELORS, 'Bachelors'),
                    (MASTERS, 'Masters'),
                    (PHD, 'PHD')
           )

    course_code = models.CharField('Course ID', max_length=200)
    course_name = models.CharField(max_length=200)
    course_type = models.CharField(max_length=30, choices=CTYPE_CHOICES)
    course_cricos_id = models.CharField('CRICOS ID', max_length=200)
    course_semester = models.CharField("Course semester", max_length=50)
    course_start_date = models.DateField("Course start date")
    application_deadline = models.DateField("Course deadline date")
    faculty_name = models.CharField("Faculty", max_length=50)
    areaofstudy = models.ManyToManyField(AreaOfStudy)
    fees = models.CharField( max_length=10, verbose_name="Fees")
    duration = models.CharField(max_length=10, verbose_name="Duration")
    educationalinstitution = models.ForeignKey(EducationInstitute)
