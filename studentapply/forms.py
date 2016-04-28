# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class StudentApplyPersonalInformation(forms.Form):

        # Uni-form
    def __init__(self, *args, **kwargs):
        super(StudentApplyPersonalInformation, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-studentApplyPersonalInformation'
        self.helper.form_class = 'studentForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('student_name', css_class='input-xlarge'),
            Field('student_address', rows="3", css_class='input-xlarge'),
            Field('student_DOB', css_class='input-xlarge'),
            Field('student_phone', css_class='input-xlarge'),
            Field('student_email', css_class='input-xlarge'),
#           'radio_buttons',
#           Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
#           AppendedText('appended_text', '.00'),
#           PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
#           PrependedText('prepended_text_two', '@'),
#            'education_level_select',
            FormActions(
                Submit('save_changes', '保存'),
                Submit('next_step', '下步', css_class="btn-primary"),
                Submit('cancel', '取消'),
            )
        )
    student_name = forms.CharField(label='姓名')

    student_address = forms.CharField(label='地址',
        widget = forms.Textarea(),
    )
    student_phone = forms.IntegerField(label='电话')
    student_DOB = forms.DateField(label='出生日期')
    student_email = forms.EmailField(label='邮箱地址')

#    radio_buttons = forms.ChoiceField(
#        choices = (
#            ('option_one', "Option one is this and that be sure to include why it's great"),
#            ('option_two', "Option two can is something else and selecting it will deselect option one")
#        ),
#        widget = forms.RadioSelect,
#        initial = 'option_two',
#    )

#    checkboxes = forms.MultipleChoiceField(
#        choices = (
#            ('option_one', "Option one is this and that be sure to include why it's great"),
#            ('option_two', 'Option two can also be checked and included in form results'),
#            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
#        ),
#        initial = 'option_one',
#        widget = forms.CheckboxSelectMultiple,
#        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#    )

#    appended_text = forms.CharField(
#        help_text = "Here's more help text"
#    )

#    prepended_text = forms.CharField()

#    prepended_text_two = forms.CharField()



class StudentApplyEducationInformation(forms.Form):

        # Uni-form
    def __init__(self, *args, **kwargs):
        super(StudentApplyEducationInformation, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-studentApplyEducationInformation'
        self.helper.form_class = 'studentForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'education_level_select',
            FormActions(
                Submit('save_changes', '保存'),
                Submit('next_step', '下步', css_class="btn-primary"),
                Submit('cancel', '取消'),
            )
        )

    education_level_select = forms.MultipleChoiceField(
    choices = (('1', '初中'), ('2', '高中'), ('3', '专科'), ('4', '本科'), ('5', '研究生')),
    )

#    radio_buttons = forms.ChoiceField(
#        choices = (
#            ('option_one', "Option one is this and that be sure to include why it's great"),
#            ('option_two', "Option two can is something else and selecting it will deselect option one")
#        ),
#        widget = forms.RadioSelect,
#        initial = 'option_two',
#    )

#    checkboxes = forms.MultipleChoiceField(
#        choices = (
#            ('option_one', "Option one is this and that be sure to include why it's great"),
#            ('option_two', 'Option two can also be checked and included in form results'),
#            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
#        ),
#        initial = 'option_one',
#        widget = forms.CheckboxSelectMultiple,
#        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#    )

#    appended_text = forms.CharField(
#        help_text = "Here's more help text"
#    )

#    prepended_text = forms.CharField()

#    prepended_text_two = forms.CharField()


class StudentApplyDocuments(forms.Form):
            # Uni-form
     def __init__(self, *args, **kwargs):
        super(StudentApplyDocuments, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-studentApplyDocuments'
        self.helper.form_class = 'studentForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            '',
            FormActions(
                Submit('save_changes', '保存'),
                Submit('next_step', '下步', css_class="btn-primary"),
                Submit('cancel', '取消'),
            )
        )

