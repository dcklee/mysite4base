from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from roles.models import Profile
from consultantregistration.models import CourseConsultantRelationship, ConsultantPersonalAssistantAssign, ConsultantRegistrationDetails
from .models import EnlingoPackageCustomer, EnlingoPackageCustomerBillingDetails, EnlingoPackageMember
#from rolepermissions.verifications import has_role
#from mysite4base.roles import Student, Consultant, ConsultantAssistant

# Pinax Blog Section Admin Class Field Verification
from pinax.blog.models import Section
from coursesearch.models import AreaOfStudy

#Define new Course and Consultant Relationships admin
class CourseConsultantRelationshipAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Consultant', {'fields': ['consultant', 'course_rep', 'outlook_statement']})
    ]
    # Form filter for "consultant_1" field who is being assigned a Consultant Assistant by Admin staff.
    # Only users who have role (urole) of Consultant can be selected
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'consultant':
                kwargs["queryset"] = Profile.objects.filter(urole="C")
        return super(CourseConsultantRelationshipAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#Define a new Consultant Personal Assistant Assignment admin
class ConsultantPersonalAssistantAssignAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Consultant Personal Assistant',{'fields': ['consultant','consultantassistant','reason']})
    ]
    # Form filter for "consultantassistant" field who is being assigned a Consultant Assistant by Admin staff.
    # Only users who have role (urole) of Consultant Assistant can be selected
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'consultantassistant':
                kwargs["queryset"] = Profile.objects.filter(urole="CA")
        if db_field.name == 'consultant':
                kwargs["queryset"] = Profile.objects.filter(urole="C")
        return super(ConsultantPersonalAssistantAssignAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


#Define a new Consultant Professional Registration Details admin
class ConsultantRegistrationDetailsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Consultant Registration Details', {'fields': [
                                                    'consultant',
                                                    'location',
                                                    'registration_qualifications',
                                                    'association',
                                                    'academic_qualifications',
                                                    'position',
                                                    'prior_work_position',
                                                    'prior_work_company_name',
                                                    'cities_lived_worked_in'
                                                    ]
    })
    ]
    # Form filter for "consultant_3" field who is has their profile created/updated by Admin staff.
    # Only users who have role (urole) of Consultant can be selected.
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'consultant':
                kwargs["queryset"] = Profile.objects.filter(urole="C")
        return super(ConsultantRegistrationDetailsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#following class creates choices field for Pinax Blog Section Model (name field) with data sourced from Area Of Study

class AOSSectionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AOSSectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = AreaOfStudy.objects.all()

    # Form filter for "name" field who is being assigned a new blog section by Admin staff.
    # Section name must be restricted to existing Area Of Study Model entries

    class Meta:
        model = Section
        fields = ['name', 'slug']

    name = forms.ModelChoiceField(queryset=None, to_field_name='name')

class AOSSectionAdmin(admin.ModelAdmin):

    form = AOSSectionForm

    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
         ('Area Of Study Blog Sections',{'fields': ['name', 'slug']})
    ]


#Register CourseConsultantRelationship,Consultant Personal Assistant Assign
admin.site.register(CourseConsultantRelationship, CourseConsultantRelationshipAdmin)
admin.site.register(ConsultantPersonalAssistantAssign, ConsultantPersonalAssistantAssignAdmin)
admin.site.register(ConsultantRegistrationDetails, ConsultantRegistrationDetailsAdmin)

admin.site.register(EnlingoPackageCustomer)
admin.site.register(EnlingoPackageCustomerBillingDetails)
admin.site.register(EnlingoPackageMember)

#Pinax Blog Admin customised fieldsets
admin.site.unregister(Section)
admin.site.register(Section, AOSSectionAdmin)
