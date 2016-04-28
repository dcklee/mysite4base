from django.test import TestCase

import datetime
# Create your tests here.
from django.contrib.auth.models import User
from django.conf import settings

from mysite4base.roles import Student, Consultant, ConsultantAssistant
from rolepermissions.verifications import has_permission

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from roles.models import Profile
from account import views
# Create your views here.

# class checkRolesTest(TestCase):
#
#     def test_check_user_Student(self):
#         user = User.objects.create_user('student9')
#         Student.assign_role_to_user(user)
#         self.assertEqual(has_permission(user, 'apply_course'), True) # Student test role has role (group) Student
#         self.assertEqual(has_permission(user, 'accept_student'), False) # Student-Role does not have role (group) Consultant
#         self.assertEqual(has_permission(user, 'review_application'), False) # Student-Role does not have role (group) Consultant
#
#     def test_check_user_Consultant(self):
#         user = User.objects.create_user('consultant9')
#         Consultant.assign_role_to_user(user)
#         self.assertEqual(has_permission(user, 'apply_course'), False) # Consultant does not have role (group) Student
#         self.assertEqual(has_permission(user, 'accept_student'), True) # Consultant has role (group) Consultant
#         self.assertEqual(has_permission(user, 'review_application'), True)  # Consultant has role (group) Consultant
#
#     def test_check_user_ConsultantAssistant(self):
#         user = User.objects.create_user('consultantassistant9')
#         ConsultantAssistant.assign_role_to_user(user)
#         self.assertEqual(has_permission(user, 'apply_course'), False) # ConsultantAssistant does not have role (group) Student
#         self.assertEqual(has_permission(user, 'accept_student'), False) # ConsultantAssistant does not have role (group) Consultant
#         self.assertEqual(has_permission(user, 'review_application'), True) # ConsultantAssistant does not have role (group) Consultant
#
#
#     def test_consultantprofile(self):
#
#         @receiver(post_save, sender=settings.AUTH_USER_MODEL, weak=False)
#         def handle_user_save(sender, instance, created, **kwargs):
#             if created:
#                 Profile.objects.create(user=instance)
# #                                            dateofbirth="1991-10-10",
# #                                            Sex="M",
# #                                            phone="1",
# #                                            address_1="1",
# #                                            address_2="2",
# #                                            city="NSW",
# #                                            state="NSW",
# #                                            postcode="2000"
#
#         User.objects.create_user('consultantassistant9')
#
#
#         u = User.objects.get(username='consultantassistant9')
#         s = Profile.objects.get(user=u)
#         v = s.user.username
#         h = User.objects.get(username=v)
#         u.first_name = s.user.first_name
#         h.first_name="Damien"
#         z = u.profile
#         z.dateofbirth='1991-10-10-09'
#         z.state = "VIC"
#         self.assertEqual(v, 'consultantassistant9')
#         self.assertEqual(u.profile.state, 'VIC')
#         self.assertEqual(h.first_name, "Damien")

# class assignRolesTest(TestCase):
#
#     def test_admin_user_role(self):
#         @receiver(post_save, sender=settings.AUTH_USER_MODEL, weak=False)
#         def handle_user_save(sender, instance, created, **kwargs):
#             if created:
#                 Profile.objects.create(user=instance)
#
#         @receiver(post_save, sender=Profile)
#         def update_role(sender, instance, created, **kwargs):
#             if created:
#                 userobj = instance
#                 user = User.objects.get(username=userobj)
#                 urolevalue = user.profile.urole
#                 user.first_name = "2@2.com"
#                 if urolevalue == "S":
#                     Student.assign_role_to_user(user)
#                 if urolevalue == "C":
#                     Consultant.assign_role_to_user(user)
#                 if urolevalue == "CA":
#                     ConsultantAssistant.assign_role_to_user(user)
#                     user.first_name = "3@3.com"
#             return
#         User.objects.create_user('consultantassistant9')
#         u = User.objects.get(username='consultantassistant9')
#         s = Profile.objects.get(user=u)
#         s.urole = "CA"
#         s.save()
#
#         user1 = User.objects.get(username='consultantassistant9')
#         self.assertEqual(user1.profile.urole, 'CA')
#         self.assertEqual(user1.first_name, '3@3.com')
#         self.assertEqual(has_permission(user1, 'apply_course'), False) # ConsultantAssistant does not have role (group) Student
#         self.assertEqual(has_permission(user1, 'accept_student'), False) # ConsultantAssistant does not have role (group) Consultant
#         self.assertEqual(has_permission(user1, 'review_application'), True) # ConsultantAssistant does not have role (group) Consultant

