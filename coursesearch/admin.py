from django.contrib import admin
from django.contrib.auth.models import User
from coursesearch.models import EducationInstitute, AreaOfStudy, Course

#Define a new EducationInstitute admin
class EducationInstituteAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Educational Insitution', {'fields': ['name', 'provider_number', 'website','city','campus','country']})
    ]

#Define a new AreaOfStudy admin
class AreaOfStudyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Area Of Study', {'fields': ['name','fontlogo']})
    ]

#Define a new Course admin
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Course', {'fields': [
                                'course_code',
                                'course_name',
                                'course_type',
                                'course_cricos_id',
                                'course_semester',
                                'course_start_date',
                                'application_deadline',
                                'faculty_name',
                                'fees',
                                'duration',
                                'areaofstudy',
                                'educationalinstitution'
                                ]
                    })
    ]

#Register EducationInsitute, AreaOfStudy, Course Admin
admin.site.register(EducationInstitute, EducationInstituteAdmin)
admin.site.register(AreaOfStudy, AreaOfStudyAdmin)
admin.site.register(Course, CourseAdmin)


