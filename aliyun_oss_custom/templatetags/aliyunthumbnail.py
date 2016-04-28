from django import template
from mysite4base.student_settings import ALIYUN_OSS_THUMBNAILS_URL
from roles.models import Profile



register = template.Library()

@register.simple_tag
def locate_image_location(object, whq):

# object refers to the profile object (one to one to Django User Object).
# whq is a hack job string referring to the Width/Height/Quality code for the Aliyun OSS Image.
# A dedicated developer can refin this custom tag later with proper parser, token and node functions.
    try:
        image = str(Profile.objects.get(pk=object.pk).profile_image)
    except Profile.DoesNotExist:
        image = ""
    query = whq
    image_type = strip_image_extension(image)
    image_url = ALIYUN_OSS_THUMBNAILS_URL+image+query+image_type
    return image_url

def strip_image_extension(image):
    #This function stips the last three extension digits from the profile_image filename and returns this for the Aliyun_OSS_Image thunmbnail model
    profile_image_tail = image[-4:]
    if profile_image_tail == ".jpg":
        image_type = ".jpg"
    elif profile_image_tail == ".png":
        image_type = ".png"
    elif profile_image_tail ==".gif":
        image_type = ".gif"
    else:
        image_type = ""
    return image_type
