from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views import generic

from configuration.models import APM, PM, TM, UI

##
#  Index Views
class APMIndexView(generic.ListView):
	model = APM
	template_name = 'configuration/index.html'

	def get_context_data(self, **kwargs):
		context = super(APMIndexView, self).get_context_data(**kwargs)
		context['model_name'] = 'APM'
		return context

class PMIndexView(generic.ListView):
	model = PM
	template_name = 'configuration/index.html'

	def get_context_data(self, **kwargs):
		context = super(PMIndexView, self).get_context_data(**kwargs)
		context['model_name'] = 'PM'
		return context

class TMIndexView(generic.ListView):
	model = TM
	template_name = 'configuration/index.html'

	def get_context_data(self, **kwargs):
		context = super(TMIndexView, self).get_context_data(**kwargs)
		context['model_name'] = 'TM'
		return context

class UIIndexView(generic.ListView):
	model = UI
	template_name = 'configuration/index.html'

	def get_context_data(self, **kwargs):
		context = super(UIIndexView, self).get_context_data(**kwargs)
		context['model_name'] = 'UI'
		return context
##
#  Detail Views
class APMDetailView(generic.DetailView):
	model = APM
	template_name = 'configuration/detail.html'

	def get_context_data(self, **kwargs):
		context = super(APMDetailView, self).get_context_data(**kwargs)
		context['model_name'] = 'APM'
		return context

class PMDetailView(generic.DetailView):
	model = PM
	template_name = 'configuration/detail.html'

	def get_context_data(self, **kwargs):
		context = super(PMDetailView, self).get_context_data(**kwargs)
		context['model_name'] = 'PM'
		return context

class TMDetailView(generic.DetailView):
	model = TM
	template_name = 'configuration/detail.html'

	def get_context_data(self, **kwargs):
		context = super(TMDetailView, self).get_context_data(**kwargs)
		context['model_name'] = 'TM'
		return context

class UIDetailView(generic.DetailView):
	model = UI
	template_name = 'configuration/detail.html'

	def get_context_data(self, **kwargs):
		context = super(UIDetailView, self).get_context_data(**kwargs)
		context['model_name'] = 'UI'
		return context

'''
def UIDetail(request, ui_id):
	item = APM.objects.get(id=ui_id)
	template = loader.get_template('configuration/detail.html')
	context = RequestContext(request, {
		'ui_id': ui_id,
		'item': item,
		'model_name': 'UI',
		})
	return HttpResponse(template.render(context))
'''

##
#  Table Views
class APMTableView(generic.ListView):
	model = APM
	template_name = 'configuration/table.html'

	def get_context_data(self, **kwargs):
		context = super(APMTableView, self).get_context_data(**kwargs)
		context['model_name'] = 'APM'
		return context

class PMTableView(generic.ListView):
	model = PM
	template_name = 'configuration/table.html'

	def get_context_data(self, **kwargs):
		context = super(PMTableView, self).get_context_data(**kwargs)
		context['model_name'] = 'PM'
		return context

class TMTableView(generic.ListView):
	model = TM
	template_name = 'configuration/table.html'

	def get_context_data(self, **kwargs):
		context = super(TMTableView, self).get_context_data(**kwargs)
		context['model_name'] = 'TM'
		return context

class UITableView(generic.ListView):
	model = UI
	template_name = 'configuration/table.html'

	def get_context_data(self, **kwargs):
		context = super(UITableView, self).get_context_data(**kwargs)
		context['model_name'] = 'UI'
		return context

def HomePageView(request):
	names = object.__class__.name__
	return HttpResponse(context)
