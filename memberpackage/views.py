from django.shortcuts import render
from django.views import generic

from . models import EnlingoPackage, EnlingoCreditRecharge
# Create your views here.

class PackageView(generic.ListView):

    model = EnlingoPackage
    template_name = 'customer_packages.html'

    def get_context_data(self, **kwargs):
        context = super(PackageView, self).get_context_data(**kwargs)
        context['soho'] = EnlingoPackage.objects.get(packageid="SOHO_001")
        context['agency'] = EnlingoPackage.objects.get(packageid="AGENCY_001")
        context['agencyplus'] = EnlingoPackage.objects.get(packageid="AGENCYPLUS_001")
        context['educationinstitute'] = EnlingoPackage.objects.get(packageid="EDUCATIONINSTITUTE_001")
        return context

    def get_queryset(self):
        super(PackageView, self).get_queryset()
        packagelist = EnlingoPackage.objects.all()
        return packagelist

class RechargeCreditsView(generic.ListView):

    model = EnlingoPackage
    template_name = 'customer_credits.html'

    def get_context_data(self, **kwargs):
        context = super(RechargeCreditsView, self).get_context_data(**kwargs)
        context['REC_500'] = EnlingoCreditRecharge.objects.get(rechargeid="REC_500")
        context['REC_500_amount'] = context['REC_500'].amount * 100
        context['REC_1000'] = EnlingoCreditRecharge.objects.get(rechargeid="REC_1000")
        context['REC_1000_amount'] = context['REC_1000'].amount * 100
        context['REC_2500'] = EnlingoCreditRecharge.objects.get(rechargeid="REC_2500")
        context['REC_2500_amount'] = context['REC_2500'].amount * 100
        context['REC_5000'] = EnlingoCreditRecharge.objects.get(rechargeid="REC_5000")
        context['REC_5000_amount'] = context['REC_5000'].amount * 100
        return context

    def get_queryset(self):
        super(RechargeCreditsView, self).get_queryset()
        rechargecreditlist = EnlingoCreditRecharge.objects.all()
        return rechargecreditlist