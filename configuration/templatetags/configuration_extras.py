from django import template
from django.template.defaultfilters import stringfilter
from itertools import *

register = template.Library()

@register.filter(name='get_unique_name')
@stringfilter
def  get_unique_name(value):
	try:
		temp = value.split('(')
	except ValueError:
		raise template.TemplateSyntaxError('unique name unavailable')
	return temp[0]

@register.filter(name='get_count')
@stringfilter
def get_count(value):
	try:
		temp = value.split(';')
	except ValueError:
		raise template.TemplateSyntaxError('filter did not encounter ";"')
	return str(len(temp))

@register.filter(name='get_first')
@stringfilter
def get_first(value):
	try:
		temp = value.split(';')
	except ValueError:
		raise template.TemplateSyntaxError('filter did not encounter ";"')
	return temp[0]

@register.filter(name='get_other')
@stringfilter
def get_other(value):
	try:
		temp = value.split(';')
	except ValueError:
		raise template.TemplateSyntaxError('filter did not encounter ";"')
	return temp[1:]

@register.assignment_tag
def get_combine_list(string1, string2):
	list1 = string1.split(';')
	list2 = string2.split(';')
	list1 = list1[1:]
	list2 = list2[1:]
	return izip_longest(list1, list2, fillvalue='')
