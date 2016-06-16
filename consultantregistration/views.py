from django.shortcuts import get_object_or_404, render
import random
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from consultantregistration.models import ConsultantRegistrationDetails, CourseConsultantRelationship
from coursesearch.models import Course
from pinax.blog.models import Post
from django.contrib.auth.models import User
from roles.models import Profile

class ConsultantListView(generic.ListView):

    model = Profile
    template_name = 'consultantregistration/Consultant_Profile_List.html'

    def get_context_data(self, **kwargs):
        #Context Data for Consultant Profile and Course
        context = super(ConsultantListView, self).get_context_data(**kwargs)
        # context['regdetails'] = self.object_list.consultantregistrationdetails.registration_qualifications
        # context['acadetails'] = self.object_list.consultantregistrationdetails.academic_qualifications
        # context['workdetails'] = self.object_list.consultantregistrationdetails.prior_work_experience
        # context['lived'] = self.object_list.consultantregistrationdetails.cities_lived_worked_in
        # context['location'] = self.object_list.consultantregistrationdetails.location
        return context

    def get_queryset(self):
        return Profile.objects.filter(urole='C')

class RegistrationView(generic.DetailView):

    model = Profile

    template_name = 'consultantregistration/Course_Consultant_Profile.html'
#       def get_context_data(self, **kwargs):
#       context = super(RegistrationView, self).get_context_data(**kwargs)
#       context['teacher'] = self.object.consultant.user.last_name
#       context['outlook'] = CourseConsultantRelationship.objects.get(consultant_1=self.object.consultant)
#       return context

    def get_context_data(self, **kwargs):
        #Context Data for Consultant Profile and Course
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['teacher'] = self.object.user.last_name
        context['email'] = self.object.user.email
        context['regdetails'] = self.object.consultantregistrationdetails.registration_qualifications
        context['acadetails'] = self.object.consultantregistrationdetails.academic_qualifications
        context['position'] = self.object.consultantregistrationdetails.position
        context['workposition'] = self.object.consultantregistrationdetails.prior_work_position
        context['lived'] = self.object.consultantregistrationdetails.cities_lived_worked_in
        context['location'] = self.object.city
        try:
            context['enlingoposts'] = Post.objects.filter(author=self.object.user).order_by("published")
            if context['enlingoposts']:
                context['current_enlingopost'] = context['enlingoposts'][0]
            else:
                context['current_enlingopost'] = ''
        except Post.DoesNotExist:
            pass
        return context
