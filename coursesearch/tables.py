import django_tables2 as tables
from coursesearch.models import AreaOfStudy, Course
from roles.models import Profile
from consultantregistration.models import ConsultantRegistrationDetails
from django_tables2 import A
from django.core.urlresolvers import reverse
from django.utils.html import mark_safe
class CourseDetailTable(tables.Table):
    id = tables.Column(verbose_name="专业编号 Course ID", visible=False)
    course_code = tables.Column(verbose_name="专业编号 Course Code")
    course_start_date = tables.Column(verbose_name="专业开学 Course Start Date")
    application_deadline = tables.Column(verbose_name="申请截止 Application Deadline")
    faculty_name = tables.Column(verbose_name="专科部门 Faculty Name")
    fees = tables.Column(verbose_name="学费 Fees")
    duration = tables.Column(verbose_name="学期期间 Duration")

    class Meta:
        model = Course
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        exclude = ("course_name", "educationalinstitution", "areaofstudy", "course_type")

class CourseListTable(tables.Table):

    id = tables.Column(verbose_name="专业编号 Course ID", visible=False)
    educationalinstitution = tables.Column(verbose_name="学校 Institution")
    course_semester = tables.Column(verbose_name="专业学期 Course Semester")
    course_type = tables.Column(verbose_name="文凭 Certification")
    areaofstudy = tables.Column(accessor='areaofstudy.id', verbose_name='Area of Studya')
    course_name = tables.LinkColumn('coursesearch:cs-course', args=[A('pk'), A('pk')], verbose_name="课程 Course Name")
    city = tables.Column(accessor='educationalinstitution.city', verbose_name="城市 City")


    # def render_aosfake(self, value, table):
    #     name = ""
    #     oFirst = True
    #     if table.Meta.slug == '[all]':
    #         orgs = value.filter(published=True, organization_type__visible=True)
    #     else:
    #         orgs = value.filter(organization_type__slug__iexact=table.Meta.slug,published=True)
    #
    #     for o in orgs:
    #         if not oFirst:
    #             name += "<br />"
    #         else:
    #             oFirst = False
    #
    #         uri = reverse('org-detail', args=[o.id])
    #         name += '<a href="' + uri + '">' + o.name + '</a>'
    #
    #     return mark_safe(name)


    class Meta:
        model = Profile
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        exclude = ('campus', 'duration', 'faculty_name', 'application_deadline',
                   'course_start_date', 'fees', 'course_semster', 'course_cricos_id', 'course_code')

class CourseConsultantProfileTable(tables.Table):

    id = tables.Column(verbose_name="专业编号 Course ID", visible=False)
    registration_qualifications = tables.Column(verbose_name="资质信息 Registration Details")
    academic_qualifications = tables.Column(verbose_name="学历背景 Academic Qualifications")
    prior_work_experience = tables.Column(verbose_name="前几行业经验 Prior Work Experience")
    location = tables.Column(verbose_name='居住城市 City of Residence')
    cities_lived_worked_in = tables.Column(verbose_name="居住城市 Places Lived/Worked")

    class Meta:
        model = ConsultantRegistrationDetails
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
