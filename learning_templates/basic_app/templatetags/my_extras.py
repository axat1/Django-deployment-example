from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all the value of 'args' from string
    """
    return value.replace(arg, '')


# register.filter('cut', cut)  # first is 'filter_name' second is fumction_name
