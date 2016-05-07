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
from mysite4base import student_settings_dev
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sites.models import Site
from django.views.generic import TemplateView
from roles import signals
from django.contrib import admin

from roles.views import SignupViewStudent, LoginView
from coursesearch.views import HomeView


urlpatterns = [
    url(r"^$", HomeView.as_view(), name="home"),
    url(r'^search/',include('haystack.urls')), #search template for development purposes only
    url(r'^country/',include('coursesearch.urls')),
    url(r'^areaofstudy/',include('coursesearch.urls', namespace="coursesearch")),
    url(r'^consultant_profile/',include('consultantregistration.urls', namespace="consultantregistration")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/signup/$', SignupViewStudent.as_view(), name="student_account_signup"),
    url(r'^account/login/$', LoginView.as_view(), name="account_login"),
#    url(r'^account/signup/$', views.SignupViewConsultant.as_view(), name="consultant_account_signup"), #placemarker for demo
#    url(r'^account2/signup/$', views.SignupViewConsultantAssistant.as_view(), name="consultant_assistant_account_signup"), #placemarker for demo
    url(r'^account/', include('account.urls')),
    url(r"^blog/", include("pinax.blog.urls")),
    url(r'^flows/', include('studentapply.urls'))
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if student_settings_dev.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += staticfiles_urlpatterns()
    # media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)