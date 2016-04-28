from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from coursesearch.models import AreaOfStudy, EducationInstitute, Course
from django.contrib.auth.models import User
from consultantregistration.models import CourseConsultantRelationship
from roles.models import Profile
from .views import AreaStudyView

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@d.com', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('areaofstudy/1/1/1/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test my_view() as if it were deployed at /customer/details
        response = AreaStudyView.as_view()(request)
        self.assertEqual(response.status_code, 200)

