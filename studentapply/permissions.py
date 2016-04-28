from rolepermissions.permissions import register_object_checker
from mysite4base.roles import Student, Consultant, SystemAdmin

@register_object_checker()
def commence_application(role, user, application):
    if role == Student:
        return True

 #   if user.application == application:
 #       return True

    return False

def review_application(role, user, application):
    if role == Consultant:
        return True

 #   if user.application == application:
 #       return True

    return False
