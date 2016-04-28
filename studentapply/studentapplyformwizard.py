from __future__ import unicode_literals

from django import forms
from django.shortcuts import render_to_response

from multipleformwizard import SessionMultipleFormWizardView

from .forms import StudentApplyPersonalInformation, StudentApplyEducationInformation, StudentApplyDocuments

class Wizard(SessionMultipleFormWizardView):
    form_list = [
        ("user_info", StudentApplyPersonalInformation),
        ("education_info", (
            ('education', StudentApplyEducationInformation),
            ('attachments', StudentApplyDocuments)
          )
        )
    ]

    templates = {
        "user_info": 'user_info.html',
        "education_info": 'education_info.html'
    }

    def get_template_names(self):
        return [self.templates[self.steps.current]]

    def done(self, form_dict, **kwargs):
        result = {}

        for key in form_dict:
            form_collection = form_dict[key]
            if isinstance(form_collection, forms.Form):
                result[key] = form_collection.cleaned_data
            elif isinstance(form_collection, dict):
                result[key] = {}
                for subkey in form_collection:
                    result[key][subkey] = form_collection[subkey].cleaned_data

        return render_to_response('demo/wizard-end.html', {
            'form_data': result,
        })