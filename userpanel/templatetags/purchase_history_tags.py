from django import template
from memberpackage.models import EnlingoPackage, EnlingoCreditRecharge


register = template.Library()

@register.simple_tag
def locate_item_description(invoice):
    try:
        item_description = EnlingoPackage.objects.get(packageid=invoice.description).description
    except EnlingoPackage.DoesNotExist:
        try:
            item_description = EnlingoCreditRecharge.objects.get(rechargeid=invoice.description).description
        except EnlingoCreditRecharge.DoesNotExist:
            item_description = ""
    return item_description