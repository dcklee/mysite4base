from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from django.contrib.auth.models import User

from roles.models import Profile#, StudentProfile, ConsultantAssistantProfile
                                # Assign custom common user profile for consultant,
                                # student and consultantassistant

#from mysite4base.roles import Student, Consultant, ConsultantAssistant
from django.contrib.auth.admin import UserAdmin

# @receiver(post_save, sender=settings.AUTH_USER_MODEL, weak=False)
# def handle_user_save(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)