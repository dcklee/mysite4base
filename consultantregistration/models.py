from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sites.models import Site

from localflavor.au.models import AUStateField, AUPhoneNumberField, AUPostCodeField

from account.models import Account
from roles.models import Profile
from coursesearch.models import Course, EducationInstitute
from memberpackage.models import EnlingoPackage
from memberpackage.models import EnlingoCreditRecharge

# Create your models here.

class CourseConsultantRelationship(models.Model):

    consultant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="consultantcourse", verbose_name="Consultant") # one to one with consultant profile
    course_rep = models.ForeignKey(Course, related_name="courserep", verbose_name='Course Representative') #consultant can "sell" these courses
    outlook_statement = models.TextField("Course Outlook") #consultant sales statement on course/industry

    def __str__(self):
        user_email = User.objects.get(pk=self.consultant.user.pk).email
        return str(user_email)

    class Meta:
        verbose_name = _("Enlingo Member Course Service Professional")
        verbose_name_plural = _("Enlingo Member Course Service Professionals")
        unique_together = ("consultant", "course_rep")

class ConsultantPersonalAssistantAssign(models.Model):
    class Meta:
        verbose_name = _("Enlingo Package Member Member Manager")
        verbose_name_plural = _("Enlingo Package Member Member Managers")

    def __str__(self):
        user_email = User.objects.get(pk=self.consultant.user.pk).email
        return str(user_email)

    consultant = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='Consultant', verbose_name="Consultant") # one to one with consultant profile
    consultantassistant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ConsultantAssistant', verbose_name="Consultant Assistant") #match consultant to consultant assistant
    reason = models.CharField(max_length=20, verbose_name="Referral Source", null=True)

class ConsultantRegistrationDetails(models.Model):
    class Meta:
        verbose_name = _("Enlingo Member Profile Details")
        verbose_name_plural = _("Enlingo Member Profile Details")

    def __str__(self):
        user_email = User.objects.get(pk=self.consultant.user.pk).email
        return str(user_email)

    consultant = models.OneToOneField(Profile, on_delete=models.CASCADE,verbose_name="Consultant") # one to one with consultant profile
    location = models.CharField('Location', max_length=20) #consultant work area
    registration_qualifications = models.CharField('Professional Qualifications', max_length=50) #consultant qualifications
    association = models.CharField('Membership Association', max_length=50) #consultant membership association
    academic_qualifications = models.CharField("Academic Qualifications", max_length=50) #consultant academic qualifications
    position = models.CharField("Position", max_length=30) #consultant work position
    prior_work_position = models.CharField("Prior Work Position", max_length=30) #consultant prior work position
    prior_work_company_name = models.CharField("Prior Workplace Name", max_length=20) #consultant prior workplace
    cities_lived_worked_in = models.CharField("Cities worked or lived in", max_length=20) #consultant places lived at

class EnlingoPackageCustomer(models.Model):
    class Meta:
        verbose_name = _("Enlingo Package Customer")
        verbose_name_plural = _("Enlingo Package Customers")

    def __str__(self):
        return str(self.customername)
    customername = models.CharField("Customer Name",max_length=50, null=True)
    customerlogo = models.ImageField(upload_to='customerlogo/', null=True)
    website = models.CharField("Web Site", max_length=50, null=True)
    education_institute = models.ManyToManyField(EducationInstitute, blank=True)
    phone = models.CharField(_("phone"), max_length=15, null=True)
    address_1 = models.CharField(_("address"), max_length=50, null=True)
    address_2 = models.CharField(_("address cont'd"), max_length=50, null=True)
    city = models.CharField(_("city"), max_length=50, null=True)
    state = AUStateField(_("state"), null=True)
    postcode = AUPostCodeField(_("postcode"), null=True)
    packadmin = models.OneToOneField(Profile, on_delete=models.CASCADE)
    package = models.ForeignKey(EnlingoPackage, on_delete=models.CASCADE, null=True)
    autorecharge = models.BooleanField()
    schemeregister = models.BooleanField()
    creditbalance = models.IntegerField(null=True)
    rechargeindicator = models.IntegerField(null=True)
    credits = models.IntegerField(null=True)
    debits = models.IntegerField(null=True)

    def recharge_needed(self):
        return self.rechargeindicator >= self.balance

class EnlingoPackageCustomerBillingDetails(models.Model):
    class Meta:
        verbose_name = _("Enlingo Package Customer Billing Details")
        verbose_name_plural = _("Enlingo Package Customer Billing Details")

    def __str__(self):
        return str(self.group)
    group = models.OneToOneField(EnlingoPackageCustomer, on_delete=models.CASCADE, null=True)
    billing_name = models.CharField("Name", max_length=20)
    billing_address_country = models.CharField("Country", max_length=20)
    billing_address_zip = models.CharField("Zip", max_length=10)
    billing_address_state = models.CharField("State", max_length=20)
    billing_address_line1 = models.CharField("Address Line 1", max_length=50)
    billing_address_city = models.CharField("City", max_length=20)

class EnlingoPackageMember(models.Model):
    class Meta:
        verbose_name = _("Enlingo Package Member")
        verbose_name_plural = _("Enlingo Package Members")

    def __str__(self):
        return str(self.member)
    member = models.OneToOneField(Profile, on_delete=models.CASCADE)
    customer_account = models.ForeignKey(EnlingoPackageCustomer, on_delete=models.CASCADE, null=True)
