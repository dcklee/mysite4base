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
from mysite4base import member_settings_dev
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sites.models import Site
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from roles import signals
from django.contrib import admin

from roles.views import SignupViewConsultant, LoginView
from userpanel.views import HomeRedirectView, MemberHome, EnlingoPremiumMember, CreditRecharge
from memberpackage.views import PackageView, RechargeCreditsView

urlpatterns = [
    #url(r"^$", TemplateView.as_view(template_name="about.html"), name="home"),
    url(r"^$", HomeRedirectView.as_view(), name="home"),
    url(r"^about/", TemplateView.as_view(template_name="about.html"), name="about"),
    url(r"^social_media_packages/", TemplateView.as_view(template_name="social_media_packages.html"), name="social_media_packages"),
    url(r"^sales_commissions_program/", TemplateView.as_view(template_name="sales_commissions_program.html"), name="sales_commissions_program"),
    url(r"^faqs/", TemplateView.as_view(template_name="faq.html"), name="faq"),
    url(r"^customerpackages/", PackageView.as_view(), name="customer_packages"),
    url(r"^rechargecredits/", RechargeCreditsView.as_view(), name="recharge_credits"),
    url(r"^rechargecreditsprocessing/(?P<rechargeid>[0-9]+)/$", CreditRecharge.as_view(), name="recharge_credits_processing"),
    url(r'subscribe/(?P<package>[0-9]+)/$', EnlingoPremiumMember.as_view(), name="subscription_wizard"),
    url(r"^memberhome/", MemberHome.as_view(), name="memberhome"),
    url(r"^company/", TemplateView.as_view(template_name="company.html"), name="company"),
    url(r"^management/", TemplateView.as_view(template_name="management.html"), name="management"),
    url(r"^userpanel/", include('userpanel.urls', namespace="userpanel")),
    url(r"^news/", TemplateView.as_view(template_name="blog.html"), name="news"),
    url(r"^contact/", TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^country/',include('coursesearch.urls')),# temp placemaker for testing pre cloud arena implementation
    url(r'^areaofstudy/',include('coursesearch.urls', namespace="coursesearch")), # temp placemaker for testing pre cloud arena implementation
    url(r'^consultant_profile/',include('consultantregistration.urls', namespace="consultantregistration")), # temp placemaker for testing pre cloud arena implementation
    url(r'^account/signup/$', SignupViewConsultant.as_view(), name="consultant_account_signup"),
    url(r'^account/login/$', LoginView.as_view(), name="account_login"),
    url(r'^payments/', include("pinax.stripe.urls")),
#    url(r'^account2/signup/$', views.SignupViewConsultantAssistant.as_view(), name="consultant_assistant_account_signup"), #placemarker for demo
    url(r"^blog/", include("pinax.blog.urls")),
    url(r"^newsletter/", include('newsletter.urls')),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^account/', include('account.urls')),
    url(r"^invites/", include("pinax.invitations.urls")),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if member_settings_dev.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += staticfiles_urlpatterns()
    # media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)