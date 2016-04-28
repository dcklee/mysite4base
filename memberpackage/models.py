from django.db import models
import datetime
import itertools

from django.core.exceptions import ImproperlyConfigured
from django.db import models, transaction, IntegrityError
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class EnlingoPackage(models.Model):
    def __str__(self):
        return str(self.packageid)
    """
    Enlingo Membership Package Type Model
    """
        #course type Items Attributes for "course_type" field: eg bachelor
    AUD = 'AUD'
    CNY = "CNY"
    USD = "USD"
    EUR = 'EUR'
    GBP = "GBP"
    HKD = 'HKD'
    SGD = "SGD"

    CURRENCY_CHOICES = ((AUD, 'Australian Dollar'),
                    (CNY, 'Renminbi'),
                    (USD, 'US Dollar'),
                    (EUR, 'Euro'),
                    (GBP, 'Pound Sterling'),
                    (HKD, 'HK Dollar'),
                    (SGD, 'Singapore Dollar')

           )

    packageid = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    credits = models.IntegerField()
    useraccountlimit = models.IntegerField()

class EnlingoCreditRecharge(models.Model):
    def __str__(self):
        return str(self.rechargeid)
    """
    Enlingo Membership Package Type Model
    """
    # course type Items Attributes for "course_type" field: eg bachelor
    AUD = 'AUD'
    CNY = "CNY"
    USD = "USD"
    EUR = 'EUR'
    GBP = "GBP"
    HKD = 'HKD'
    SGD = "SGD"

    CURRENCY_CHOICES = ((AUD, 'Australian Dollar'),
                        (CNY, 'Renminbi'),
                        (USD, 'US Dollar'),
                        (EUR, 'Euro'),
                        (GBP, 'Pound Sterling'),
                        (HKD, 'HK Dollar'),
                        (SGD, 'Singapore Dollar')

                        )

    rechargeid = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    credits = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)


class CreditValue(models.Model):

    def __str__(self):
        return str(self.creditaccount)
    """
    Credit Cost Model
    """
            #course type Items Attributes for "course_type" field: eg bachelor
    AUD = 'AUD'
    CNY = "CNY"
    USD = "USD"
    EUR = 'EUR'
    GBP = "GBP"
    HKD = 'HKD'
    SGD = "SGD"

    CURRENCY_CHOICES = ((AUD, 'Australian Dollar'),
                    (CNY, 'Renminbi'),
                    (USD, 'US Dollar'),
                    (EUR, 'Euro'),
                    (GBP, 'Pound Sterling'),
                    (HKD, 'HK Dollar'),
                    (SGD, 'Singapore Dollar')

           )

    creditaccount = models.OneToOneField(EnlingoPackage, on_delete=models.CASCADE)
    creditvalue = models.DecimalField(max_digits=4, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)