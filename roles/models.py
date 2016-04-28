from django.db import models

from django.contrib.auth.models import AnonymousUser
from django.contrib.sites.models import Site

from account.models import Account
from django.contrib.auth.models import User
from account.conf import settings
from django.utils.translation import ugettext as _
from localflavor.au.models import AUStateField, AUPhoneNumberField, AUPostCodeField
from localflavor.cn import cn_provinces

from coursesearch.models import Course
# Create your models here.

#Exend user model for each role type, student, consultant or personalassistant

#class AustralianAddress(models.Model):

#    address_1 = models.CharField(_("address"), max_length=128)
#    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
#    city = models.CharField(_("city"), max_length=64)
#    state = AUStateField(_("state"))
#    postcode = AUPostCodeField(_("postcode"))

# class StudentProfile(models.Model):
#     def __str__(self):
#         return str(self.user.username)
#     #Gender Items Attributes for "Sex" gender field
#     MALE = 'M'
#     FEMALE = 'F'
#     NEUTER = 'N'
#     SEX_CHOICES = ((MALE, 'Male'),
#                     (FEMALE, 'Female'),
#                     (NEUTER, 'Neuter')
#            )
#     #Salutation
#
#     MR = "Mr"
#     MISS = "Miss"
#     MS = "Ms"
#     DR = "Dr"
#
#     SALUTATION_CHOICES = ((MR, 'Mr'),
#                           (MISS, 'Miss'),
#                           (MS, 'Ms'),
#                           (DR, "Dr")
#                           )
#     # This field is required
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     #Essential Info for Student
#     salutation = models.CharField(max_length=4, choices=SALUTATION_CHOICES, null=True)
#     dateofbirth = models.DateField(null=True)
#     Sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE, null=True)
#     phone = models.CharField(_("phone"), max_length=15, null=True)
#     address_1 = models.CharField(_("address"), max_length=128, null=True)
#     address_2 = models.CharField(_("address cont'd"), max_length=128, null=True)
#     city = models.CharField(_("city"), max_length=64, null=True)
#     provinces = models.CharField(max_length=6, null=True)
#     postcode = models.CharField(_("postcode"), max_length=6, null=True)

class Profile(models.Model):
    def __str__(self):
        return str(self.user.username)
    #Gender Items Attributes for "Sex" gender field
    MALE = 'M'
    FEMALE = 'F'
    NEUTER = 'N'
    SEX_CHOICES = ((MALE, 'Male'),
                    (FEMALE, 'Female'),
                    (NEUTER, 'Neuter')
                     )

    #Salutation

    MR = "Mr"
    MISS = "Miss"
    MS = "Ms"
    DR = "Dr"

    SALUTATION_CHOICES = ((MR, 'Mr'),
                          (MISS, 'Miss'),
                          (MS, 'Ms'),
                          (DR, "Dr")
                          )

    #Role for user admin to see

    STUDENT = "S"
    CONSULTANT = "C"
    CONSULTANT_ASSISTANT = "CA"

    ROLE_CHOICES = ((STUDENT, 'Student'),
                          (CONSULTANT, 'Consultant'),
                          (CONSULTANT_ASSISTANT, 'Consultant Assistant')
                          )
    # This field is required
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #Essential Info for Consultant
    salutation = models.CharField(max_length=4, choices=SALUTATION_CHOICES, null=True)
    dateofbirth = models.DateField(null = True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True)
    phone = models.CharField(_("phone"), max_length=15, null=True)
    address_1 = models.CharField(_("address"), max_length=50, null=True)
    address_2 = models.CharField(_("address cont'd"), max_length=50, null=True)
    city = models.CharField(_("city"), max_length=50, null=True)
    state = AUStateField(_("state"), null=True)
    postcode = AUPostCodeField(_("postcode"), null=True)
    profile_image = models.ImageField(upload_to='profile/')
    urole = models.CharField(_("User Role"), max_length=20, choices=ROLE_CHOICES, null=True) #django_role_permissions related field
# class ConsultantAssistantProfile(models.Model): #25/03/2016 Not used yet
#     def __str__(self):
#         return str(self.user.username)
#     #Gender Items Attributes for "Sex" gender field
#     MALE = 'M'
#     FEMALE = 'F'
#     NEUTER = 'N'
#     SEX_CHOICES = ((MALE, 'Male'),
#                     (FEMALE, 'Female'),
#                     (NEUTER, 'Neuter')
#            )
#
#     #Salutation
#
#     MR = "Mr"
#     MISS = "Miss"
#     MS = "Ms"
#     DR = "Dr"
#
#     SALUTATION_CHOICES = ((MR, 'Mr'),
#                           (MISS, 'Miss'),
#                           (MS, 'Ms'),
#                           (DR, "Dr")
#                           )
#
#     # This field is required
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     #Essential Info for Consultant Assistant
#     salutation = models.CharField(max_length=4, choices=SALUTATION_CHOICES, null=True)
#     dateofbirth = models.DateField(null=True)
#     Sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE, null=True)
#     phone = models.CharField(_("phone"), max_length=15, null=True)
#     address_1 = models.CharField(_("address"), max_length=128, null=True)
#     address_2 = models.CharField(_("address cont'd"), max_length=128, null=True)
#     city = models.CharField(_("city"), max_length=64, null=True)
#     provinces = models.CharField(max_length=6, null=True)
#     postcode = models.CharField(_("postcode"), max_length=6, null=True)



