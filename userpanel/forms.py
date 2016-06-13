from django import forms
from django.forms import formset_factory, modelformset_factory
from django.utils import timezone
from django.utils.functional import curry
from django.utils.translation import ugettext_lazy as _

from pinax.blog.conf import settings
from pinax.blog.models import Post, Revision
from pinax.blog.utils import can_tweet, load_path_attr
from pinax.blog.signals import post_published

from django.contrib.auth.models import User
from consultantregistration.models import EnlingoPackageCustomer, EnlingoPackageMember
from roles.models import Profile
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import TextInput, Select
from localflavor.au.forms import AUPhoneNumberField, AUPostCodeField, STATE_CHOICES

FIELDS = [
    "section",
    "author",
    "markup",
    "title",
    "slug",
    "teaser",
    "content",
    "description",
    "primary_image",
    "state",
]

if can_tweet():
    FIELDS.append("tweet")


class MemberPostForm(forms.ModelForm):

    title = forms.CharField(
        label=_("Title"),
        max_length=90,
        widget=forms.TextInput(attrs={"style": "width: 50%;"}),
    )
    slug = forms.CharField(
        label=_("Slug"),
        widget=forms.TextInput(attrs={"style": "width: 50%;"})
    )
    teaser = forms.CharField(
        label=_("Teaser"),
        widget=forms.Textarea(attrs={"style": "width: 80%;"}),
    )
    content = forms.CharField(
        label=_("Content"),
        widget=forms.Textarea(attrs={"style": "width: 80%; height: 300px;"})
    )
    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea(attrs={"style": "width: 80%;"}),
        required=False
    )
    if can_tweet():
        tweet = forms.BooleanField(
            required=False,
            help_text=_("Checking this will send out a tweet for this post"),
            label=_("Can tweet?"),
        )

    class Meta:
        model = Post
        fields = FIELDS

    class Media:
        js = ("js/admin_post_form.js",)

    def __init__(self, *args, **kwargs):
        super(MemberPostForm, self).__init__(*args, **kwargs)

        post = self.instance

        # grab the latest revision of the Post instance
        latest_revision = post.latest()

        if latest_revision:
            # set initial data from the latest revision
            self.fields["teaser"].initial = latest_revision.teaser
            self.fields["content"].initial = latest_revision.content

    def save(self):
        published = False
        post = super(MemberPostForm, self).save(commit=False)

        if post.pk is None or Post.objects.filter(pk=post.pk, published=None).count():
            if self.cleaned_data["state"] == Post.STATE_CHOICES[-1][0]:
                post.published = timezone.now()
                published = True

        render_func = curry(
            load_path_attr(
                settings.PINAX_BLOG_MARKUP_CHOICE_MAP[self.cleaned_data["markup"]]["parser"]
            )
        )

        post.teaser_html = render_func(self.cleaned_data["teaser"])
        post.content_html = render_func(self.cleaned_data["content"])
        post.updated = timezone.now()
        post.save()

        r = Revision()
        r.post = post
        r.title = post.title
        r.teaser = self.cleaned_data["teaser"]
        r.content = self.cleaned_data["content"]
        r.author = post.author
        r.updated = post.updated
        r.published = post.published
        r.save()

        if can_tweet() and self.cleaned_data["tweet"]:
            post.tweet()

        if published:
            post_published.send(sender=Post, post=post)

        return post

class EnlingoMemberSubcribe(forms.Form):

    #Gender Items Attributes for "Sex" gender field
    MALE = 'M'
    FEMALE = 'F'
    NEUTER = 'N'
    SEX_CHOICES = ((MALE, 'Male'),
                   (FEMALE, 'Female'),
                   (NEUTER, 'Neuter')
                   )
    salutation = forms.CharField(widget=TextInput)
    firstname = forms.CharField(label='First Name', widget=TextInput)
    surname = forms.CharField(widget=TextInput)
    profile_image = forms.ImageField(widget=forms.ClearableFileInput)
    # birthdate = forms.DateField() #Post Subsription Used Field
    # sex = forms.ChoiceField(widget=Select, choices=SEX_CHOICES) #Post Subscription Used Field
    # phone = AUPhoneNumberField()
    # address_1 = forms.CharField(widget=TextInput)
    # address_2 = forms.CharField(widget=TextInput, required="")
    city = forms.CharField(widget=TextInput)
    # postcode = AUPostCodeField()
    # state = AUStateSelect()
    companyname = forms.CharField(label='Company Name') # Name of Company
    registrationqualifications = forms.CharField(label='Professional Qualifications') #consultant qualifications
    autorecharge = forms.BooleanField(label='Auto Recharge', required=False)
    schemeregister = forms.BooleanField(label='Scheme Registration', required=False)
    #academicqualifications = forms.CharField(label="Academic Qualifications") #consultant academic qualifications
    #priorworkexperience = forms.CharField(label="Prior Work Experience") #consultant prior work experience
    #citieslivedworkedin = forms.CharField(label="Cities worked or lived in") #consultant places lived at

class EnlingoMemberUpdate(forms.Form):

    #Salutation

    MR = "Mr"
    MISS = "Miss"
    MS = "Ms"
    DR = "Dr"

    SALUTATION_CHOICES = ((MR, 'Mr'),
                          (MISS, 'Miss'),
                          (MS, 'Ms'),
                          (DR, "Dr")
                          )
    #Gender Items Attributes for "Sex" gender field
    MALE = 'M'
    FEMALE = 'F'
    NEUTER = 'N'
    SEX_CHOICES = ((MALE, 'Male'),
                   (FEMALE, 'Female'),
                   (NEUTER, 'Neuter')
                   )
    last_name = forms.CharField(
        label=_("Surname"),
        max_length=30,
        widget=forms.TextInput(),
        required=True
    )
    first_name = forms.CharField(
        label=_("First Name"),
        max_length=30,
        widget=forms.TextInput(),
        required=True
    )
    profile_image = forms.ImageField(widget=forms.ClearableFileInput)
    salutation = forms.ChoiceField(widget=Select, choices=SALUTATION_CHOICES)
    birthdate = forms.DateField() #Post Subsription Used Field
    sex = forms.ChoiceField(widget=Select, choices=SEX_CHOICES) #Post Subscription Used Field
    phone = AUPhoneNumberField()
    address_1 = forms.CharField(widget=TextInput)
    address_2 = forms.CharField(widget=TextInput, required="")
    city = forms.CharField(widget=TextInput)
    postcode = AUPostCodeField()
    state = forms.ChoiceField(widget=Select, choices=STATE_CHOICES)

class EnlingoPackageMemberDeactivateForm(forms.Form):

    email = forms.EmailField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    deactivate = forms.BooleanField(label='Deactivate Account', required=False)

EnlingoPackageMemberDeactivateFormSet = formset_factory(EnlingoPackageMemberDeactivateForm,
                                                             extra=0)

class EnlingoRechargeCreditProcessing(forms.Form):

    email1 = forms.CharField(widget = forms.TextInput, required=False)

class EnlingoPostWeeklyQuiz(forms.Form):
    #Pinax Blog Section displayed as hidden "Area of Study" field in userpanel
    section = forms.CharField(widget = forms.TextInput)
    #Pinax Blog Title displayed as "Institution" Name field for data collection purposes
    title = forms.CharField(widget = forms.TextInput)
    #Pinax Blog Description displayed as "Post" field in userpanel
    description = forms.CharField(widget=forms.TextInput)
    #Pinax Announcements Announcement ID displayed as hidden "announcement_id" field in userpanel
    announcement_id = forms.CharField(widget=forms.TextInput)