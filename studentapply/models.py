from django.db import models
from viewflow.models import Process
# Create your models here.

class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

class StudentApply(Process):
    text = models.CharField('Course ID', max_length=150) # to be foreign key from Course App database
    approved = models.BooleanField('Successful Submit', default=False)