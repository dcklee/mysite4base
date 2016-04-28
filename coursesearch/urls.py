
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.CountrySearchView.as_view(), name="country"), # for country search showcasing purposes only
    url(r'^(?P<studyarea>[0-9]+)/$', views.AreaStudyView.as_view(), name="areastudy"),
    url(r'^(?P<studyarea>[0-9]+)/(?P<course1>[0-9]+)/$', views.CourseDetailView.as_view(), name="course"),
    url(r'^(?P<studyarea>[0-9]+)/(?P<course1>[0-9]+)/(?P<consultant1>[0-9]+)/$', views.CourseConsultantChatView.as_view(), name="courseconsultant"),
    url(r'^(?P<studyarea>[0-9]+)/(?P<course1>[0-9]+)/(?P<consultant1>[0-9]+)/courseconsultant/$', views.RegistrationReferralView.as_view(), name="r_course_consultant_profile")

]