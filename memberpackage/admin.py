from django.contrib import admin

from .models import EnlingoPackage
from .models import EnlingoCreditRecharge
from .models import CreditValue


admin.site.register(EnlingoPackage)
admin.site.register(EnlingoCreditRecharge)
admin.site.register(CreditValue)
