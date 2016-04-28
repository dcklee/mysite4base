from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import TextInput, Select
from localflavor.au.forms import AUPhoneNumberField, AUPostCodeField, STATE_CHOICES
import account.forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class SignupFormStudent(account.forms.SignupForm):

    #Gender Items Attributes for "Sex" gender field
    MALE = 'M'
    FEMALE = 'F'
    NEUTER = 'N'
    SEX_CHOICES = ((MALE, 'Male'),
                   (FEMALE, 'Female'),
                   (NEUTER, 'Neuter')
                   )
    salutation = forms.CharField(widget=TextInput)
    firstname = forms.CharField(label='First Name', widget=TextInput)
    surname = forms.CharField(widget=TextInput)
    birthdate = forms.DateField()
    sex = forms.ChoiceField(widget=Select, choices=SEX_CHOICES)
    phone = AUPhoneNumberField()
    address_1 = forms.CharField(widget=TextInput)
    address_2 = forms.CharField(widget=TextInput, required="")
    city = forms.CharField(widget=TextInput)
    postcode = AUPostCodeField()
    state = forms.ChoiceField(widget=Select, choices=STATE_CHOICES)



# class SignupFormConsultant(account.forms.SignupForm):
#
#     def __init__(self, *args, **kwargs):
#         super(SignupFormConsultant, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'signup_form'
#         self.helper.form_class = 'form loginRegistrationForm'
#         self.helper.form_method = 'post'
#         self.helper.form_action = 'consultant_account_signup'
#         self.helper.layout = Layout(
#             Field('email', template="index.html")
#         )
#
#         self.helper.add_input(Submit('submit', 'Submit'))



