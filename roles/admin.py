from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


from django.contrib.auth.models import User, Group, Permission
from roles.models import Profile#, ConsultantProfile, ConsultantAssistantProfile
#from mysite4base.roles import Student, Consultant, ConsultantAssistant
from django.forms.widgets import CheckboxInput
from django import forms

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


from six import add_metaclass


from django.contrib.contenttypes.models import ContentType

#Define an inline admin descriptor for StudentProfile model
#which acts a bit like a singleton

# class StudentProfileInline(admin.StackedInline):
#     model = StudentProfile
#     can_delete = False
#     verbose_name_plural = 'studentprofile'

#Define an inline admin descriptor for StudentProfile model
#which acts a bit like a singleton

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

#Define an inline admin descriptor for StudentProfile model
#which acts a bit like a singleton

# class ConsultantAssistantProfileInline(admin.StackedInline):
#     model = ConsultantAssistantProfile
#     can_delete = False
#     verbose_name_plural = 'consultantassistantprofile'

#Define a new User admin
class UserAdmin(UserAdmin):

    inlines = (ProfileInline,) #ConsultantProfileInline, ConsultantAssistantProfileInline)

#useradmin function to update assignment of user role using django_roles_permissions, includes the business process to assign ConsultantAssistant role
    def save_related(self, request, form, formsets, change):
        super(UserAdmin, self).save_related(request, form, formsets, change)
        uprofile = form.instance
        user = User.objects.get(username=uprofile.username)
        urolevalue = user.profile.urole
        if urolevalue == "S":
            self.change_role(user, 'student')
        if urolevalue == "C":
           self.change_role(user, 'consultant')
        if urolevalue == "CA":
            self.change_role(user, 'consultant_assistant')
        uprofile.save()

        #Deletes all of user's previous roles.
        #:returns: :py:class:`django.contrib.auth.models.Group` The group for the
        #    new role.
    def change_role(self, user, groupname):
        group = user.groups.filter(name__in=["student","consultant", "consultant_assistant"])
        for role in group:
            user.groups.remove(role)
        group, created = Group.objects.get_or_create(name=groupname)
        user.groups.add(group)
        return


#Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)