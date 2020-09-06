from django import template

register = template.Library()
@register.filter(name='cutt')
def cut(value,arg):
    """
    This cuts out all the values from teh string
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')

# register.filter('cutt', cut)