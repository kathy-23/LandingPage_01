from django import template

register = template.library()

@register.assignment_tag
def hello_world(name):
    salute='Hello' + name
    return salute

