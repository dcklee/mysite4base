"""mysite3base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.sites.models import Site
from django.views.generic import TemplateView
from roles import signals
from django.contrib import admin

from roles import views

urlpatterns = [
    # url(r'^payments/', include("pinax.stripe.urls")),
    # url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    # url(r'^consultant_profile/',include('consultantregistration.urls', namespace="consultantregistration")),
    # url(r'^areaofstudy/',include('coursesearch.urls', namespace="coursesearch")),
#    url(r'^areaofstudy/$', TemplateView.as_view(template_name="AreaOfStudy_Business.html"), name="area_study"),
#    url(r'^areaofstudy/course/$', TemplateView.as_view(template_name="Course_Consultant_Details.html"), name="course"),
#    url(r'^areaofstudy/course/consultant/', TemplateView.as_view(template_name="Consultant_Course_Chat.html"), name="course_chat"),
#    url(r'^consultant_profile/', TemplateView.as_view(template_name="Course_Consultant_Profile.html"), name="course_consultant_profile"),
#     url(r'^admin/', include(admin.site.urls)),
#    url(r'^account/signup/$', views.SignupViewStudent.as_view(), name="student_account_signup"),
#    url(r'^account/signup/$', views.SignupViewConsultant.as_view(), name="consultant_account_signup"), #placemarker for demo
#    url(r'^account2/signup/$', views.SignupViewConsultantAssistant.as_view(), name="consultant_assistant_account_signup"), #placemarker for demo
#     url(r'^account/', include('account.urls')),
#     url(r"^blog/", include("pinax.blog.urls")),
#\    url(r'^flows/', include('studentapply.urls'))
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)