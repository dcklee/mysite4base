from __future__ import unicode_literals
import decimal
import datetime

from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render, render_to_response
from django.utils.http import base36_to_int, int_to_base36
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateResponseMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic import View, TemplateView, DetailView, ListView
from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.models import User, Group
from . import forms
from consultantregistration.models import ConsultantRegistrationDetails, EnlingoPackageCustomer, EnlingoPackageCustomerBillingDetails, EnlingoPackageMember
from coursesearch.models import EducationInstitute
from pinax.invitations.models import InvitationStat
from django.contrib import auth, messages
#from django.contrib.sites.models import get_current_site
from django.contrib.auth.tokens import default_token_generator

from account import signals
from account.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from account.conf import settings
from account.utils import default_redirect, get_form_data
from account.models import AccountDeletion

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from pinax.blog.models import Post, Section
from pinax.announcements.models import Announcement
from pinax.stripe.models import Customer, Charge
from pinax.stripe.actions import customers, charges, sources
from pinax.stripe.mixins import CustomerMixin, PaymentsContextMixin

from memberpackage.models import EnlingoPackage, EnlingoCreditRecharge

# Create your views here.
#If non-authenticated user, show this page
class HomeRedirectView(RedirectView):
    permanent = False

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect("consultant_account_signup")
        else:
            return redirect("memberhome")
        #return super(HomeRedirectView, self).get(*args, **kwargs)

#If consultant is logged in, show this page
class MemberHome(TemplateView):
    template_name = "index.html"

    # check user has consultant access
    @method_decorator(permission_required('consultantregistration.add_consultantregistrationdetails', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(MemberHome, self).dispatch(request, *args, **kwargs)

class PostCreate(SuccessMessageMixin, CreateView):
    template_name = "userpanel/blog/post_add.html"
    model = Post
    success_url = reverse_lazy('userpanel:userpanel_main')
    success_message = "Post Created"
    fields = [
        "section",
        "title",
        "description",
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    # Django permissions_required decorator to ensure user is authorised as enlingo_premium_member to access this view
    @method_decorator(permission_required('blog.add_post', raise_exception=True))
    # @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return super(PostCreate, self).dispatch(request, *args, **kwargs)

class PostUpdate(SuccessMessageMixin, UpdateView):
    template_name = "userpanel/blog/post_edit.html"
    model = Post
    success_url = reverse_lazy('userpanel:userpanel_main')
    success_message = "Post Edited"
    fields = [
    "section",
    "title",
    "description",
]

    def get_object(self, queryset=None):
        """Hook to ensure object is owned by request.user. """
        obj= super(PostUpdate, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj

    # Django permissions_required decorator to ensure user is authorised as enlingo premium_member to access this view
    @method_decorator(permission_required('blog.change_post', raise_exception=True))
    # @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)
    # Django login_required decorator superceded by permissions_required check
    # @method_decorator(login_required(login_url='/account/login'))
    # def dispatch(self, request, *args, **kwargs):
    #     self.request = request
    #     self.args = args
    #     self.kwargs = kwargs
    #     return super(PostUpdate, self).dispatch(request, *args, **kwargs)

class PostDelete(SuccessMessageMixin, DeleteView):
    template_name = "userpanel/blog/post_delete.html"
    model = Post
    success_url = reverse_lazy('userpanel:userpanel_main')
    success_message = "Post Deleted"

    # Django permissions_required decorator to ensure user is authorised as enlingo premium_member to access this view
    @method_decorator(permission_required('blog.delete_post', raise_exception=True))
    # @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return super(PostDelete, self).dispatch(request, *args, **kwargs)

    # Django login_required decorator superceded by permissions_required check
    # @method_decorator(login_required(login_url='/account/login'))
    # def dispatch(self, request, *args, **kwargs):
    #     self.request = request
    #     self.args = args
    #     self.kwargs = kwargs
    #     return super(PostDelete, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """Hook to ensure object is owned by request.user. """
        obj= super(PostDelete, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj

class MemberPost(View):

    def get(self, request, *args, **kwargs):
        view = MemberPostPanel.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = EnlingoPostWeeklyQuizSave.as_view()
        return view(request, *args, **kwargs)

class MemberPostPanel(ListView):

    template_name = "userpanel/userpanel.html"
    #form_class = forms.EnlingoPostWeeklyQuiz
    identifier_field = "username"
    messages = {
        "email_confirmation_sent": {
            "level": messages.INFO,
            "text": _("Confirmation email sent to {email}.")
        },
        "invalid_signup_code": {
            "level": messages.WARNING,
            "text": _("The code {code} is invalid.")
        }
    }
    # check user has consultant access to access userpanel
    @method_decorator(permission_required('consultantregistration.add_consultantregistrationdetails', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(MemberPostPanel, self).dispatch(request, *args, **kwargs)

    def __init__(self, **kwargs):
        super(MemberPostPanel, self).__init__(**kwargs)

    # Django login_required decorator superceded by Pinax Account Login_Required Mixin
    # @method_decorator(login_required(login_url='/account/login'))
    # def dispatch(self, request, *args, **kwargs):
    #     self.request = request
    #     self.args = args
    #     self.kwargs = kwargs
    #     return super(MemberPost, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MemberPostPanel, self).get_context_data(**kwargs)
        memberposts = Post.objects.filter(author = self.request.user)
        try:
            credits = EnlingoPackageCustomer.objects.get(enlingopackagemember__member=self.request.user.profile).creditbalance
        except EnlingoPackageCustomer.DoesNotExist:
            credits = "0"
        context['memberposts'] = memberposts
        context['creditbalance'] = credits
        context['form'] = forms.EnlingoPostWeeklyQuiz()
        context['institutelist'] = EducationInstitute.objects.filter(country="AU") #temporarily hardcode country filter
        return context

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class EnlingoPostWeeklyQuizSave(SingleObjectMixin, FormView):
    template_name = 'userpanel/userpanel.html'
    form_class = forms.EnlingoPostWeeklyQuiz
    success_url = reverse_lazy('userpanel:userpanel_main')

    #userpanel.html post http header processing
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return super(EnlingoPostWeeklyQuizSave, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EnlingoPostWeeklyQuizSave, self).get_context_data(**kwargs)
        memberposts = self.get_queryset()
        try:
            credits = EnlingoPackageCustomer.objects.get(enlingopackagemember__member=self.request.user.profile).creditbalance
        except EnlingoPackageCustomer.DoesNotExist:
            credits = "0"
        context['memberposts'] = memberposts
        context['creditbalance'] = credits
        return context

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        self.save_weekly_enlingo_post(form)
        self.dismiss_weekly_enlingo_post(form)
        if hasattr(auth, "update_session_auth_hash"):
            auth.update_session_auth_hash(self.request, self.request.user)
        return super(EnlingoPostWeeklyQuizSave, self).form_valid(form)

    # Check and Update Weekly Enlingo Post
    def save_weekly_enlingo_post(self, form):
        section = Section.objects.get(name=form.cleaned_data['section'])
        #Create Pinax Blog Post Instance
        weeklyenlingopost = Post.objects.create(author=self.request.user,
                                                section=section,
                                                description=form.cleaned_data["description"],
                                                title=form.cleaned_data["title"]
                                                )
        return weeklyenlingopost

    def dismiss_weekly_enlingo_post(self, form):
        if self.request.user.is_authenticated():
            announcement = Announcement.objects.get(pk = form.cleaned_data['announcement_id'])
            announcement.dismissals.create(user=self.request.user)
            status = 200

class EnlingoPremiumMember(CustomerMixin, PaymentsContextMixin,SuccessMessageMixin, FormView):
    template_name = "subscription_wizard.html"
    form_class = forms.EnlingoMemberSubcribe
    pk_url_kwarg = 'package'
    success_url = '/userpanel'
    success_message = "Payment Successful"

      # check to ensure enlingo premium_member user cannot re-subscribe
    @method_decorator(login_required(login_url='account_login'))
    def dispatch(self, request, *args, **kwargs):
        member = User.objects.get(pk=self.request.user.pk)
        user_group_check = member.groups.filter(name="premium_member") # Need to softcode group keyword for adminsite administration
        # check if request.user is already a premium_member, if so redirect to userpanel
        if user_group_check.exists():
            return redirect('/userpanel')
        else:
            return super(EnlingoPremiumMember, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        #user = self.request.user
        user = User.objects.get(username=self.request.user.username)
        package_id = self.kwargs.get('package')
        package_object = get_object_or_404(EnlingoPackage,pk=package_id)
        profile = self.request.user.profile # replace with project reverse one to one profile attribute
        crdetails, created = ConsultantRegistrationDetails.objects.get_or_create(consultant=profile) #, created is to allow get_or_create to unpack immediately, from stackoverflow
        enlingo_member = self.update_enlingo_package_customer(form, profile, package_object)
        self.update_billing_details(enlingo_member)
        profile.salutation = form.cleaned_data["salutation"] #update profile optional fields not needed at initial user object creation stage
        user.first_name = form.cleaned_data["firstname"] # get User object to fill in first name
        user.last_name = form.cleaned_data["surname"] # get User object to fill in last name
        profile.profile_image = form.cleaned_data['profile_image']
        ##profile.dateofbirth = form.cleaned_data["birthdate"]
        ##profile.sex = form.cleaned_data["sex"]
        # profile.phone=form.cleaned_data["phone"]
        # profile.address_1 = form.cleaned_data["address_1"]
        # profile.address_2 = form.cleaned_data["address_2"]
        profile.city = form.cleaned_data["city"]
        # profile.state = form.cleaned_data["state"]
        # profile.postcode = form.cleaned_data["postcode"]
        crdetails.registration_qualifications = form.cleaned_data['registrationqualifications'] #consultant qualifications
        # crdetails.academic_qualifications = form.cleaned_data["academicqualifications"] #consultant academic qualifications
        # crdetails.prior_work_experience = form.cleaned_data["priorworkexperience"] #consultant prior work experience
        # crdetails.cities_lived_worked_in = form.cleaned_data["citieslivedworkedin"] #consultant places lived at
        profile.save()
        crdetails.save()
        self.create_stripe_customer(user)
        self.charge_customer(package_object)
        # required on Django >= 1.7 to keep the user authenticated
        user.groups.add(Group.objects.get(name='product_admin'))
        self.add_package_member(profile, enlingo_member)
        user.save()
        if hasattr(auth, "update_session_auth_hash"):
            auth.update_session_auth_hash(self.request, user)
        return super(EnlingoPremiumMember,self).form_valid(form)

    # Create Enlingo Premium Member Account
    def update_enlingo_package_customer(self, form, profile, package_object):
                #Create Enlingo Premium Member Package Account
        enlingomember, created = EnlingoPackageCustomer.objects.get_or_create(packadmin_id=profile.pk,
                                                                           defaults={'package_id': package_object.pk,
                                                                                     'autorecharge': form.cleaned_data["autorecharge"],
                                                                                     'schemeregister': form.cleaned_data["schemeregister"],
                                                                                     'customername': form.cleaned_data["companyname"],
                                                                                     'rechargeindicator': '10',
                                                                                     'creditbalance': package_object.credits,
                                                                                     'credits': package_object.credits,
                                                                                     'debits': '0'}) #, created is to allow get_or_create to unpack immediately, from stackoverflow
        invitations = package_object.useraccountlimit-1
        InvitationStat.add_invites_to_user(profile.user, invitations)
        return enlingomember

    # Update Enlingo Premium Member Account Billing Details
    def update_billing_details(self, enlingo_member):
        billing_name=self.request.POST['stripeBillingName']
        billing_address_line1=self.request.POST['stripeBillingAddressLine1']
        billing_address_zip=self.request.POST['stripeBillingAddressZip']
        billing_address_city=self.request.POST['stripeBillingAddressCity']
        billing_address_state=self.request.POST['stripeBillingAddressState1']
        billing_address_country=self.request.POST['stripeBillingAddressCountry']
        enlingomemberbillingaddress, created = EnlingoPackageCustomerBillingDetails.objects.get_or_create(group_id=enlingo_member.pk,
                                                                           defaults={'billing_name': billing_name,
                                                                                     'billing_address_zip': billing_address_zip,
                                                                                     'billing_address_country': billing_address_country,
                                                                                     'billing_address_state': billing_address_state,
                                                                                     'billing_address_city': billing_address_city,
                                                                                     'billing_address_line1': billing_address_line1,
                                                                                     }) #, created is to allow get_or_create to unpack immediately, from stackoverflow
        return enlingomemberbillingaddress

    #Create Stripe customer and save payment method on Stripe customer account
    def create_stripe_customer(self, user):
        try:
            Customer.objects.get(user=user)
        except Customer.DoesNotExist:
            customers.create(user=user, card=self.request.POST['stripeToken'])
        return

    #Charge customer using Pinax Stripe API
    def charge_customer(self, package_object):
        charges.create(amount=decimal.Decimal(package_object.amount),
                       customer=self.request.user.customer.stripe_id,
                       currency=package_object.currency,
                       description=package_object.packageid
                       )
        return

    # Add profile to Enlingo Premium Member Account (called enlingo_package_member)
    def add_package_member(self, profile, enlingo_member):
        enlingo_package_member, created = EnlingoPackageMember.objects.get_or_create(customer_account=enlingo_member,member=profile) #, created is to allow get_or_create to unpack immediately, from stackoverflow
        profile.user.groups.add(Group.objects.get(name='premium_member'))
        return enlingo_package_member

    def get_context_data(self, **kwargs):
        context = super(EnlingoPremiumMember, self).get_context_data(**kwargs)
        package = get_object_or_404(EnlingoPackage,pk=self.kwargs.get('package'))
        context['packageidentifier'] = package.id
        context['packagedescription'] = package.description
        context['packageamount'] = package.amount
        context['stripeamount'] = package.amount*100
        context['packagecredits'] = package.credits
        context['packagedesccription'] = package.description
        context['packageusers'] = package.useraccountlimit
        context['packagecurrency'] = package.currency
        return context

class CreditRecharge(CustomerMixin, PaymentsContextMixin, SuccessMessageMixin, FormView):
    template_name = "recharge_credits_processing.html"
    form_class = forms.EnlingoRechargeCreditProcessing
    pk_url_kwarg = 'rechargeid'
    success_url = '/userpanel'
    success_message = "Recharge Successful"

    def __init__(self, *args, **kwargs):
        super(CreditRecharge, self).__init__(*args, **kwargs)

    # check to ensure enlingo premium_member user cannot re-subscribe
    @method_decorator(login_required(login_url='account_login'))
    def dispatch(self, request, *args, **kwargs):
        member = User.objects.get(pk=self.request.user.pk)
        user_group_check = member.groups.filter(
            name="product_admin")  # Need to softcode group keyword for adminsite administration
        # check if request.user is already a premium_member, if so redirect to userpanel
        if user_group_check.exists():
            return super(CreditRecharge, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(self.get_success_url())

    def form_valid(self, form, *args, **kwargs):
        user = self.request.user
        recharge_pack = EnlingoCreditRecharge.objects.get(pk=self.kwargs.get('rechargeid'))
        self.check_stripe_customer(user)
        self.charge_customer(recharge_pack)
        self.update_enlingo_package_customer(user, recharge_pack)
        return super(CreditRecharge,self).form_valid(form)

    def check_stripe_customer(self, user):
        try:
            Customer.objects.get(user=user)
        except Customer.DoesNotExist:
            customers.create(user=user, card=self.request.POST['stripeToken'])
        return

    # Charge customer using Pinax Stripe API
    def charge_customer(self, recharge_pack):
        charges.create(amount=decimal.Decimal(recharge_pack.amount), customer=self.request.user.customer.stripe_id,
                       currency=recharge_pack.currency, description=recharge_pack.rechargeid)
        return

        # Create Enlingo Premium Member Account
    def update_enlingo_package_customer(self, user, recharge_pack):
        # Update Enlingo Premium Member Customer Package Account
        enlingomember = EnlingoPackageCustomer.objects.get(packadmin_id=user.profile.pk)
        enlingomember.creditbalance += recharge_pack.credits
        enlingomember.credits += recharge_pack.credits
        enlingomember.save()
        return

    def get_context_data(self, **kwargs):
        context = super(CreditRecharge, self).get_context_data(**kwargs)
        recharge_pack = get_object_or_404(EnlingoCreditRecharge, pk=self.kwargs.get('rechargeid'))
        context['rechargeidentifier'] = recharge_pack.id
        context['rechargedescription'] = recharge_pack.description
        context['rechargeamount'] = recharge_pack.amount
        context['stripeamount'] = recharge_pack.amount * 100
        context['rechargecredits'] = recharge_pack.credits
        context['rechargecurrency'] = recharge_pack.currency
        return context

class MemberUpdateProfile(LoginRequiredMixin, FormView):

    template_name = "userpanel/member_profile_edit.html"
    form_class = forms.EnlingoMemberUpdate
    success_url = reverse_lazy('userpanel:member-profile-edit')
    messages = {
        "profile_updated": {
            "level": messages.SUCCESS,
            "text": _("Profile settings updated")
        },
    }

    def get_initial(self):
        initial = super(MemberUpdateProfile, self).get_initial()
        initial['salutation'] = self.request.user.profile.salutation
        initial["last_name"] = self.request.user.last_name
        initial["first_name"] = self.request.user.first_name
        initial["profile_image"] = self.request.user.profile.profile_image
        initial['birthdate'] = self.request.user.profile.dateofbirth
        initial['sex'] = self.request.user.profile.sex
        initial['phone'] = self.request.user.profile.phone
        initial['address_1'] = self.request.user.profile.address_1
        initial['address_2'] = self.request.user.profile.address_2
        initial['city'] = self.request.user.profile.city
        initial['postcode'] = self.request.user.profile.postcode
        initial['state'] = self.request.user.profile.state
        return initial

    def form_valid(self, form):
        self.update_member_profile(form)
        if self.messages.get("profile_updated"):
            messages.add_message(
                self.request,
                self.messages["profile_updated"]["level"],
                self.messages["profile_updated"]["text"]
            )
        return redirect(self.get_success_url())


    def update_member_profile(self, form):
        self.update_user(form)
        self.update_profile(form)

    def update_user(self, form, confirm=None):
        user = self.request.user
        user.last_name = form.cleaned_data['last_name']  # get User object to fill in first name
        user.first_name = form.cleaned_data['first_name']  # get User object to fill in last name
        #EmailAddress.objects.add_email(self.request.user, email, primary=True, confirm=confirm)
        user.save()

    def update_profile(self, form):
        profile = self.request.user.profile # replace with project reverse one to one profile attribute
        profile.profile_image = form.cleaned_data['profile_image']
        profile.salutation = form.cleaned_data["salutation"]
        profile.dateofbirth = form.cleaned_data["birthdate"]
        profile.sex = form.cleaned_data["sex"]
        profile.phone=form.cleaned_data["phone"]
        profile.address_1 = form.cleaned_data["address_1"]
        profile.address_2 = form.cleaned_data["address_2"]
        profile.city = form.cleaned_data["city"]
        profile.postcode = form.cleaned_data["postcode"]
        profile.state = form.cleaned_data["state"]
        profile.save()

# Get Specific Profile model object for self.request.user
    def get_object(self, queryset=None):
        return self.request.user

class MemberUpdateProfessionalDetails(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "userpanel/member_professional_details_edit.html"
    model = ConsultantRegistrationDetails
    success_message = 'Member Details Updated'
    success_url = reverse_lazy('userpanel:member-professional-details-edit')
    messages = {
        "details_updated": {
            "level": messages.SUCCESS,
            "text": _("Details updated")
        },
    }
    fields = [
    "registration_qualifications",
    "academic_qualifications",
    "position",
    "prior_work_position",
    "prior_work_company_name",
    "cities_lived_worked_in",
]

# Get Specific ConsultantRegistrationDetails model object for self.request.user
    def get_object(self, queryset=None):
        return self.request.user.profile.consultantregistrationdetails


    # check user has consultant access
    @method_decorator(permission_required('consultantregistration.add_consultantregistrationdetails', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(MemberUpdateProfessionalDetails, self).dispatch(request, *args, **kwargs)

class CustomerUpdatePackageDetails(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "userpanel/customer_package_details_edit.html"
    model = EnlingoPackageCustomer
    success_url = reverse_lazy('userpanel:customer-package-details-edit')
    success_message = 'Member Package Details Updated'

    fields = [
    "customername",
    "customerlogo",
    "website",
    "education_institute",
    "phone",
    "address_1",
    "address_2",
    "city",
    "state",
    "postcode",
    "autorecharge",
    "schemeregister"
]

# Get Specific ConsultantRegistrationDetails model object for self.request.user
    def get_object(self, queryset=None):
        return self.request.user.profile.enlingopackagecustomer

    # check user has consultant access
    @method_decorator(permission_required('consultantregistration.add_consultantregistrationdetails', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(CustomerUpdatePackageDetails, self).dispatch(request, *args, **kwargs)

class CustomerUpdateBillingDetails(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "userpanel/customer_billing_details_edit.html"
    model = EnlingoPackageCustomerBillingDetails
    success_url = reverse_lazy('userpanel:customer-billing-details-edit')
    success_message = 'Member Billing Details Updated'
    fields = [
    "billing_name",
    "billing_address_country",
    "billing_address_zip",
    "billing_address_state",
    "billing_address_line1",
    "billing_address_city"
]

# Get Specific ConsultantRegistrationDetails model object for self.request.user
    def get_object(self, queryset=None):
        return self.request.user.profile.enlingopackagecustomer.enlingopackagecustomerbillingdetails

    # check user has consultant access
    @method_decorator(permission_required('consultantregistration.add_consultantregistrationdetails', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(CustomerUpdateBillingDetails, self).dispatch(request, *args, **kwargs)

class CustomerPurchaseHistory(ListView):
    template_name = "userpanel/customer_purchase_history.html"
    model = Charge

    def get_context_data(self, **kwargs):
        context = super(CustomerPurchaseHistory, self).get_context_data(**kwargs)
        charges = Charge.objects.filter(customer=self.request.user.customer)
        customer = EnlingoPackageCustomer.objects.get(packadmin=self.request.user.profile)
        context['customer'] = customer.enlingopackagecustomerbillingdetails.billing_name
        context['billingaddress_1'] = customer.enlingopackagecustomerbillingdetails.billing_address_line1
        context['billingaddress_city'] = customer.enlingopackagecustomerbillingdetails.billing_address_city
        context['billingaddress_state'] = customer.enlingopackagecustomerbillingdetails.billing_address_state
        context['billingaddress_postcode'] = customer.enlingopackagecustomerbillingdetails.billing_address_zip
        context['invoices'] = charges.order_by('-pk')
        return context

    # check user has consultant access
    @method_decorator(permission_required('consultantregistration.add_consultantregistrationdetails', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(CustomerPurchaseHistory, self).dispatch(request, *args, **kwargs)

class MemberAccountDeactivate(SuccessMessageMixin, FormView):
    template_name = "userpanel/member_group_manager_deactivate.html"
    model = EnlingoPackageMember
    form_class = forms.EnlingoPackageMemberDeactivateForm
    success_url = reverse_lazy('userpanel:member-group-manager-deactivate')
    success_message = "Member Account Deactivated"

    #Django permissions_required decorator to ensure user is authorised as enlingo premium_member to access this view
    @method_decorator(permission_required('invitations.delete_joininvitation', raise_exception=True))
    # @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return super(MemberAccountDeactivate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, formset):
        for form in formset:
            deactivate = form.cleaned_data["deactivate"]
            if deactivate is True:
                user = User.objects.get(email=form.cleaned_data["email"])
                AccountDeletion.mark(user)
        #Allocate an Enlingo Package Member quota to Customer
        InvitationStat.add_invites_to_user(self.request.user, +1)
        return super(MemberAccountDeactivate,self).form_valid(formset)

    def form_invalid(self, formset):
        return self.render_to_response(self.get_context_data(formset=formset))

    def get_context_data(self, **kwargs):
        context = super(MemberAccountDeactivate, self).get_context_data(**kwargs)
        #Return all active Enlingo Premium Members for this customer package account
        deactivate_list_initial = EnlingoPackageMember.objects.filter(customer_account_id__packadmin=self.request.user.profile.pk)
        deactivated = []
        for deactivate_list in deactivate_list_initial:
            deactivated_user_check = deactivate_list.member.user
            if deactivated_user_check.is_active is False:
                deactivated.append(deactivated_user_check.profile.pk)
        enlingoactivepackagemembers = deactivate_list_initial.exclude(member__in=deactivated).exclude(member=self.request.user.profile.pk)
        context['formset'] = forms.EnlingoPackageMemberDeactivateFormSet(initial=[{'email' : member.member.user.email,
                                                                                   'last_name' : member.member.user.last_name,
                                                                                   'first_name' : member.member.user.first_name,
                                                                                   'deactivate' : ""}
                                                                                  for member in enlingoactivepackagemembers])
        return context


    def post(self, request, *args, **kwargs):
        formset = forms.EnlingoPackageMemberDeactivateFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)
        return self.form_invalid(formset)


