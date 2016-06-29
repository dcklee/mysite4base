from django.shortcuts import render
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from account.conf import settings
import os
from account import views
from account.forms import LoginEmailForm
#from mysite4base.roles import Student, Consultant,ConsultantAssistant
from . import forms
from roles.models import Profile
from consultantregistration.models import ConsultantRegistrationDetails,EnlingoPackageCustomer, EnlingoPackageMember
from pinax.invitations.views import JoinInvitation
from account.models import signup_code_sent
# Create your views here.

class LoginView(views.LoginView): # Use email to login
    messages = {
        "login_confirmed": {
            "level": messages.SUCCESS,
            "text": _("Welcome back {username} to your Post Manager.")
        }
    }

    form_class = LoginEmailForm

    def after_login(self, form):
        self.login_message()
        super(LoginView, self).after_login(form)

    def login_message(self):
        if self.messages.get("login_confirmed"):
            messages.add_message(
                self.request,
                self.messages["login_confirmed"]["level"],
                self.messages["login_confirmed"]["text"].format(**{
                        "username": self.request.user.username
                    })
            )
        return

class SignupViewStudent(views.SignupView):

    form_class = forms.SignupFormStudent

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupViewStudent, self).after_signup(form)


    def update_profile(self, form):
        profile = self.created_user.profile # replace with project reverse one to one profile attribute
        profile.salutation = form.cleaned_data["salutation"]
        userob = User.objects.get(username=profile.user.username)
        userob.first_name = form.cleaned_data["firstname"] # get User object to fill in first name
        userob.last_name = form.cleaned_data["surname"] # get User object to fill in last name
        profile.dateofbirth = form.cleaned_data["birthdate"]
        profile.sex = form.cleaned_data["sex"]
        profile.phone=form.cleaned_data["phone"]
        profile.address_1 = form.cleaned_data["address_1"]
        profile.address_2 = form.cleaned_data["address_2"]
        profile.city = form.cleaned_data["city"]
        profile.state = form.cleaned_data["state"]
        profile.postcode = form.cleaned_data["postcode"]
        profile.urole = "S"
        profile.save()
        userob.save()
        self.created_user.groups.add(Group.objects.get(name='student'))
        return

class SignupViewConsultant(views.SignupView):

    template_name = "index.html"
    # form_class = forms.SignupFormConsultant

    #This code check if sign up code has been allocated to sign up user, if so then assign user to Enlingo membergroup
    # def use_signup_code(self, user):
    #     self.assign_non_package_member_admin_user_group(user)
    #     super(SignupViewConsultant, self).use_signup_code(user)
    #
    # def assign_non_package_member_admin_user_group(self, user):
    #     if self.signup_code_present is True:
    #         user = self.created_user
    #         user.groups.add(Group.objects.get(name='premium_member'))
    #         user.save()
    #     return

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupViewConsultant, self).after_signup(form)

    def update_profile(self, form):
        Profile.objects.create(user=self.created_user, urole="C", profile_image="site_media/media/profile/whitespace.gif")
        #profile = self.created_user.profile # replace with project reverse one to one profile attribute
        ConsultantRegistrationDetails.objects.create(consultant=self.created_user.profile)
        #user = User.objects.get(username=self.created_user.username)
        #userob = User.objects.get(username=self.created_user.username)
        #profile.urole = "C" # this field needs to be set as it demonstrates user has a role of consultant for staff use only
        #urole = "C" # this field needs to be set as it demonstrates user has a role of consultant for staff use only
        #profile.save()
        #crdetails.save()
        #userob.save()
        if self.signup_code:
            customer_account=self.locate_package_member(self.created_user)
            self.add_package_member(self.created_user, customer_account)
        #self.created_user.save()
        self.created_user.groups.add(Group.objects.get(name='consultant'))
        #Consultant.assign_role_to_user(self.created_user)

        # Locate enlingo member package account for package member
    def locate_package_member(self, user):
        account_admin = JoinInvitation.objects.get(signup_code=self.signup_code.pk).from_user
        customer_account = EnlingoPackageCustomer.objects.get(packadmin=account_admin.profile) #, created is to allow get_or_create to unpack immediately, from stackoverflow
        return customer_account

    def add_package_member(self, user, enlingo_member):
        enlingo_package_member, created = EnlingoPackageMember.objects.get_or_create(customer_account=enlingo_member,member=user.profile) #, created is to allow get_or_create to unpack immediately, from stackoverflow
        user.groups.add(Group.objects.get(name='premium_member'))
        return enlingo_package_member

# class SignupViewConsultantAssistant(views.SignupView):
#
#     form_class = forms.SignupFormConsultant
#
#     def after_signup(self, form):
#         self.update_profile(form)
#         super(SignupViewConsultantAssistant, self).after_signup(form)
#
#     def update_profile(self, form):
#         profile = self.created_user.profile # replace with project reverse one to one profile attribute
#         profile.salutation = form.cleaned_data["salutation"]
#         userob = User.objects.get(username=profile.user.username)
#         userob.first_name = form.cleaned_data["firstname"] # get User object to fill in first name
#         userob.last_name = form.cleaned_data["surname"] # get User object to fill in last name
#         profile.dateofbirth = form.cleaned_data["birthdate"]
#         profile.sex = form.cleaned_data["sex"]
#         profile.phone=form.cleaned_data["phone"]
#         profile.address_1 = form.cleaned_data["address_1"]
#         profile.address_2 = form.cleaned_data["address_2"]
#         profile.city = form.cleaned_data["city"]
#         profile.state = form.cleaned_data["state"]
#         profile.postcode = form.cleaned_data["postcode"]
#         profile.save()
#         userob.save()
#         self.created_user.groups.add(Group.objects.get(name='consultant_assistant'))
#         return
