from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic
#Coursesearch models
from coursesearch.models import AreaOfStudy, EducationInstitute, Course
#Consultant Registration models
from django.contrib.auth.models import User
from consultantregistration.models import CourseConsultantRelationship, ConsultantPersonalAssistantAssign, ConsultantRegistrationDetails
from roles.models import Profile
# django-tables2 table
from coursesearch.tables import CourseDetailTable, CourseListTable, CourseConsultantProfileTable
from django_tables2 import SingleTableMixin, SingleTableView
#Pinax Blog Models and Views
from pinax.blog.views import BlogIndexView
from pinax.blog.models import Post, Section
#haystack searchviews
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet
from coursesearch import forms


class HomeView(generic.ListView):

    model = AreaOfStudy
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        areaofstudylist = AreaOfStudy.objects.all()
        #aos_blog = Post.objects.get(pk=3) #temporary get object code.
        admin_blog = Post.objects.filter(author__username='admin') #temporary placeholder
        college_innovation_blog = Post.objects.filter(author__username='admin') #temporary placeholder
        college_news_blog = Post.objects.filter(author__username='admin') #temporary placeholder
        context['areaofstudy'] = areaofstudylist
        #context['dailyblog'] = aos_blog
        context['adminblog'] = admin_blog
        context['collegeinnovation'] = college_innovation_blog
        context['collegenews'] = college_news_blog

        return context

class AreaStudyView(generic.ListView):

    model = Course
    template_name = 'coursesearch/AreaOfStudy_Business.html'
    pk_url_kwarg = 'course1'

    # django-table2 table.py class
    # table_class = CourseListTable
    # context_table_name = 'table'

    def get_context_data(self, **kwargs):
        context = super(AreaStudyView, self).get_context_data(**kwargs)
        context['areaofstudy'] = AreaOfStudy.objects.get(pk=self.kwargs.get('studyarea'))
        context['courselist'] = self.object_list
        return context

    def get_queryset(self):
        self.areaofstudy = get_object_or_404(AreaOfStudy, pk=self.kwargs.get('studyarea'))
        return Course.objects.filter(areaofstudy=self.areaofstudy)

class CourseDetailView(generic.DetailView):

    template_name = 'coursesearch/Course_Consultant_Details.html'
    model = Course
    pk_url_kwarg = 'course1'
    # django-table2 table.py class
    # table_class = CourseDetailTable
    # context_table_name = 'table'

    def get_context_data(self, **kwargs):

        context = super(CourseDetailView, self).get_context_data(**kwargs)
        # following two django querysets return all related consultant profile objects to Course instance
        course = get_object_or_404(Course, pk=self.kwargs.get('course1'), areaofstudy=self.kwargs.get('studyarea'))
        courseconsultants = CourseConsultantRelationship.objects.filter(course_rep=course.pk)
        context['courseconsultants'] = courseconsultants
        context['course1'] = self.kwargs.get('course1')
        context['studyarea'] = self.kwargs.get('studyarea')
        return context

class CourseConsultantChatView(generic.DetailView):
#    model = CourseConsultantRelationship
    pk_url_kwarg = 'consultant1'
    template_name = 'coursesearch/Consultant_Course_Chat.html'

    def get_context_data(self, **kwargs):

        context = super(CourseConsultantChatView, self).get_context_data(**kwargs)
         #following two lines check if url is valid before proceeding with the function body
        courseid = Course.objects.get(pk = self.kwargs.get('course1')).pk
        if courseid == Course.objects.get(pk=self.kwargs.get('course1'), areaofstudy=self.kwargs.get('studyarea')).pk:
        #Display student selected consultant photo, surname and industry Outlook on Course
            courseconsultantphoto = self.object.consultant.profile_image
            courseconsultantins = self.object.consultant.user.last_name
            consultantoutlook = self.object.outlook_statement
            # following two django querysets return all related consultant user objects to Course instance
            try:
                courseconsultants1 = CourseConsultantRelationship.objects.filter(course_rep=self.kwargs.get('course1'))
                courseconsultants2 = courseconsultants1.exclude(consultant=self.kwargs.get('consultant1'))
            except CourseConsultantRelationship.DoesNotExist:
                raise Http404("No CourseConsultantRelationship matches the given query")
            courseconsultants = User.objects.filter(profile__consultantcourse=courseconsultants2)[:4]
            #Return Course name
            coursenamei = Course.objects.get(pk=self.kwargs.get('course1')).course_name
            educationinsi = Course.objects.get(pk=self.kwargs.get('course1')).educationalinstitution
            #Return Consultant Assistant Profile and Photo
            consultantassisti = ConsultantPersonalAssistantAssign.objects.get(consultant=self.kwargs.get('consultant1'))
            #Return Consultant Blogs for the area of study selected
            try:
                consultant_blog_section_aos = AreaOfStudy.objects.get(pk=self.kwargs.get('studyarea'))
                consultant_blog_section = Section.objects.get(name=consultant_blog_section_aos.name)
                post_list = Post.objects.filter(author=self.object.consultant.user, section=consultant_blog_section)
            except Post.DoesNotExist:
                raise Http404("No Post matches the given query")
            #Return consultant profile object
            conprofile = Profile.objects.get(pk=self.kwargs.get('consultant1'))
            #context results for display
            #Course representative (consultant) selected by student
            context['courseconsultantlist'] = courseconsultants
            context['courseconsultanti'] = courseconsultantins
            context['courseconsultantphoto'] = courseconsultantphoto
            context['course'] = coursenamei
            context['educationinstitution'] = educationinsi
            context['consultantassistant'] = consultantassisti.consultantassistant.user.last_name
            context['consultantassistantphoto'] = consultantassisti.consultantassistant.profile_image.url
            context['consultantoutlook'] = consultantoutlook
            context['consultantid'] = self.kwargs.get('consultant1')
            context['studyarea'] = self.kwargs.get('studyarea')
            context['courseid'] = courseid
            # Consultant blogs related to Area of Study
            context['aospost_list'] = post_list
            # Area of Study Blogs for showcasing purposes only
            context['aos_section'] = consultant_blog_section
            # Consultant Profile - ConsultantRegistrationDetails model
            context['consultant_object'] = conprofile
            context['consultantassistant_object'] = consultantassisti.consultantassistant
            context['regdetails'] = conprofile.consultantregistrationdetails.registration_qualifications
            context['acadetails'] = conprofile.consultantregistrationdetails.academic_qualifications
            context['workdetails'] = conprofile.consultantregistrationdetails.prior_work_position
            context['lived'] = conprofile.consultantregistrationdetails.cities_lived_worked_in
            context['location'] = conprofile.consultantregistrationdetails.location
            return context

    def get_object(self, queryset=None):

        return get_object_or_404(CourseConsultantRelationship,consultant=self.kwargs.get('consultant1'),
                                 course_rep=self.kwargs.get('course1')
                                 )

class RegistrationReferralView(generic.DetailView):

    model = Profile
    pk_url_kwarg = 'consultant1'
    template_name = 'consultantregistration/C_Course_Consultant_Profile.html'

        # django-table2 table.py class
    # table_class = CourseConsultantProfileTable
    # context_table_name = 'table'

    # def get_context_data(self, **kwargs):
    #     context = super(RegistrationView, self).get_context_data(**kwargs)
    #     context['teacher'] = self.object.consultant.user.last_name
    #     context['outlook'] = CourseConsultantRelationship.objects.get(consultant=self.object.consultant)
    #     return context

    def get_context_data(self, **kwargs):
        context = super(RegistrationReferralView, self).get_context_data(**kwargs)
        courseid = Course.objects.get(pk = self.kwargs.get('course1')).pk
        #Conext Data for Consultant Profile and Course
        if courseid == Course.objects.get(pk = self.kwargs.get('course1'), areaofstudy=self.kwargs.get('studyarea')).pk:
        #Display student selected consultant surname
            courseconsultantin = get_object_or_404(CourseConsultantRelationship,
                                                   course_rep=self.kwargs.get('course1'),
                                                   consultant=self.kwargs.get('consultant1'))
            courseconsultantins = User.objects.get(profile__consultantcourse__exact=courseconsultantin._get_pk_val).last_name
            # following two django querysets return all related consultant user objects to Course instance
            try:
                courseconsultants1 = CourseConsultantRelationship.objects.filter(course_rep=self.kwargs.get('course1'))
                courseconsultants2 = courseconsultants1.exclude(consultant=self.kwargs.get('consultant1'))
            except CourseConsultantRelationship.DoesNotExist:
                raise Http404("No CourseConsultantRelationship matches the given query")
            courseconsultants = User.objects.filter(profile__consultantcourse=courseconsultants2)[:4]
            #Return Course name
            coursenamei = Course.objects.get(pk=self.kwargs.get('course1')).course_name
            educationinsi = Course.objects.get(pk=self.kwargs.get('course1')).educationalinstitution
            #context results for display
            context['courseconsultantlist'] = courseconsultants
            context['courseconsultanti'] = courseconsultantins
            context['course'] = coursenamei
            context['educationinstitution'] = educationinsi
            context['consultantid'] = self.kwargs.get('consultant1')
            context['studyarea'] = self.kwargs.get('studyarea')
            context['courseid'] = courseid
            context['teacher'] = self.object.user.last_name
            context['regdetails'] = self.object.consultantregistrationdetails.registration_qualifications
            context['acadetails'] = self.object.consultantregistrationdetails.academic_qualifications
            context['workdetails'] = self.object.consultantregistrationdetails.prior_work_experience
            context['lived'] = self.object.consultantregistrationdetails.cities_lived_worked_in
            context['location'] = self.object.consultantregistrationdetails.location
            return context

class CountrySearchView(generic.ListView):

    model = Course
    template_name = 'coursesearch/Country_Search.html'

    def get_context_data(self, **kwargs):
        context = super(CountrySearchView, self).get_context_data(**kwargs)
        courselist = Course.objects.all()
        #context results for display
        context['courselist'] = courselist
        return context