from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

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
	return zip(list1, list2)

'''
@register.tag
def do_combine_list(parser, token):
	try:
		tag_name, list1, list2, var_name = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires two arguments" % token.contents.split()[0])

	list1 = list1.split(';')
	list2 = list2.split(';')
	list1 = list1[1:]
	list2 = list2[1:]
	return CombineListNode(list1, list2, var_name)

class CombineListNode(template.Node):
	def __init__(self, list1, list2, var_name):
		self.list1 = list1
		self.list2 = list2
		self.var_name = var_name
	def render(self, context):
		context[self.var_name] = zip(self.list1, self.list2)
		return ''
'''
