from django import template
from django.utils import timezone


register = template.Library()


@register.filter
def days_ago(val):
    now = timezone.now()
    delta = val - now
    plural = ''
    if abs(delta.days) != 1:
        plural = 's'
    return f'{abs(delta.days)} Day{plural} Ago ({val})'
    
