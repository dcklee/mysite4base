from django import forms
from coursesearch.models import Course, EducationInstitute

from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

# class CountryCourseSearchForm(SearchForm):
#
#     #def __init__(self, *args, **kwargs):
#      #   super(CountryCourseSearchForm, self).__init__(*args, **kwargs)
#         #self.fields['country'].queryset = EducationInstitute.objects.all()
#
#     # Form filter for "name" field who is being assigned a new blog section by Admin staff.
#     # Section name must be restricted to existing Area Of Study Model entries
#
#     #class Meta:
#     #model = EducationInstitute
#     #fields = ['name', 'city', 'country']
#
#     queryset = SearchQuerySet().filter(educationalinstitution__country='US')
#     country = forms.ModelChoiceField(max_length=100, required=False)
#     city = forms.ModelChoiceField(queryset=EducationInstitute.objects.all())
#     name = forms.ModelChoiceField(queryset=EducationInstitute.objects.all())
#
#
#     def search(self):
#         # First, store the SearchQuerySet received from other processing.
#         sqs = super(CountryCourseSearchForm, self).search()
#         if not self.is_valid():
#             return self.no_query_found()
#         # Check to see if a country was chosen.
#         if self.cleaned_data['country']:
#             sqs = sqs.filter(country=self.cleaned_data['country'])
#         # Check to see if a city was chosen.
#         if self.cleaned_data['city']:
#             sqs = sqs.filter(city=self.cleaned_data['city'])
#         # Check to see if an educational instution was chosen.
#         if self.cleaned_data['name']:
#             sqs = sqs.filter(city=self.cleaned_data['name'])
#         return sqs
