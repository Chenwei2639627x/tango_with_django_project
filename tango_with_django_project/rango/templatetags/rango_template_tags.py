from django import template
from rango.models import Category
from atexit import register

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category = None):
  return {'categories': Category.objects.all(),'current_category': current_category}

