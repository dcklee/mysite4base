import datetime
from haystack import indexes
from coursesearch.models import EducationInstitute
from haystack.query import SearchQuerySet

# class EInstitutionIndex(indexes.SearchIndex, indexes.Indexable):
#     name = indexes.CharField(model_attr='name')
#     city = indexes.CharField(model_attr='city')
#     campus = indexes.CharField(model_attr='campus')
#     text = indexes.CharField(document=True, use_template=True)
#
#     queryset = SearchQuerySet().filter(educationalinstitution__country='US')
#     def get_model(self):
#         return EducationInstitute
#
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(country=self.text)