from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.ConsultantListView.as_view(), name="consultant_list"),
    url(r'^(?P<pk>[0-9]+)/$', views.RegistrationView.as_view(), name="course_consultant_profile")
]