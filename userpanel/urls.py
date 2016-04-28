
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.MemberPost.as_view(), name="userpanel_main"), # userpanel
    url(r'author/add/$', views.PostCreate.as_view(), name='post-add'),
    url(r'author/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(), name='post-edit'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post-delete'),
    url(r'memberprofile/$', views.MemberUpdateProfile.as_view(), name='member-profile-edit'),
    url(r'memberprofessionaldetails/$', views.MemberUpdateProfessionalDetails.as_view(), name='member-professional-details-edit'),
    url(r'enlingopackagecustomer/$', views.CustomerUpdatePackageDetails.as_view(), name='customer-package-details-edit'),
    url(r'groupmemberadd/$', TemplateView.as_view(template_name="userpanel/member_group_manager_add.html"), name='member-group-manager-add'),
    url(r'groupmemberdeactivate/$',  views.MemberAccountDeactivate.as_view(), name='member-group-manager-deactivate'),
    url(r'customerbillingdetails/$', views.CustomerUpdateBillingDetails.as_view(), name='customer-billing-details-edit'),
    url(r'customerpurchasehistory/$', views.CustomerPurchaseHistory.as_view(), name='customer-purchase-history')
]
