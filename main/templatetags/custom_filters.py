from django import template

register = template.Library()

@register.filter
def custom_slice(lst, index):
    return lst[index:index+4]

from django import template

register = template.Library()

@register.filter
def star_range(value):
    return range(value)
from django import template
from django.template.defaultfilters import slugify as django_slugify

register = template.Library()

@register.filter(name='slugify')
def slugify(value):
    return django_slugify(value)