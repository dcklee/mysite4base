from __future__ import unicode_literals

from django.http import Http404, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404, render
from django.utils.http import base36_to_int, int_to_base36
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormView

from django.contrib import auth, messages
from django.contrib.auth import get_user_model
#from django.contrib.sites.models import get_current_site
from django.contrib.auth.tokens import default_token_generator

from account import signals
from account.conf import settings
from account.forms import SignupForm, LoginUsernameForm
from account.forms import ChangePasswordForm, PasswordResetForm, PasswordResetTokenForm
from account.forms import SettingsForm
from account.hooks import hookset
from account.mixins import LoginRequiredMixin
from account.models import SignupCode, EmailAddress, EmailConfirmation, Account, AccountDeletion
from account.utils import default_redirect, get_form_data

from .forms import StudentApplyPersonalInformation, StudentApplyEducationInformation
# Create your views here.

#class StudentApply(TemplateResponseMixin, View):
#def checkuserrole(request):
#        self.request = request
#      if request.user.is_authenticated():
#          user = request.user
#          role = get_user_role(user)
#      return role

def index(request):
    return render(request, 'studentapply.html', {'form': StudentApplyPersonalInformation()})



