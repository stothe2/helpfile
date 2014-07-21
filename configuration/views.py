from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views import generic

from configuration.models import APM

# Create your views here.
class IndexView(generic.ListView):
	model = APM
	template_name = 'configuration/index.html'

def detail(request, apm_id):
	item = APM.objects.get(id=apm_id)
	itemSet = item.settings.split(";")
	itemCom = item.comments.split(";")
	firstSet = itemSet[0]
	otherSet = itemSet[1:]
	firstCom = itemCom[0]
	otherCom = itemCom[1:]
	combined = zip(otherSet, otherCom)
	count = len(itemSet)
	countStr = str(count)
	template = loader.get_template('configuration/detail.html')
	context = RequestContext(request, {
		'apm_id': apm_id,
		'item': item,
		'itemSet': itemSet,
		'countStr': countStr,
		'firstSet': firstSet,
		'itemCom': itemCom,
		'firstCom': firstCom,
		'combined': combined,
		})
	return HttpResponse(template.render(context))

'''
class APMDetailView(generic.DetailView):
	model = APM
	template_name = 'configuration/detail.html'

	def get_queryset(self):
		queryset = super(APMDetailView, self).get_queryset().filter(pk=self.kwargs['pk'])
		return queryset

	def get_context_data(self, **kwargs):
		itemSet = self.get_queryset().settings.split(';')
		itemCom = comments.split(';')
		firstSet = itemSet[0]
		otherSet = itemSet[1:]
		firstCom = itemCom[0]
		otherCom = itemCom[1:]
		combined = zip(otherSet, otherCom)
		count = len(itemSet)
		countStr = str(count)

		extra_context = {
			'firstSet': firstSet,
			'firstCom': firstCom, 
			'countStr': countStr,
			'other': other,
		}

		context = super(APMDetailView, self).get_context_data(**kwargs)
		
		for key in extra_context:
			context[key] = extra_context[key]

		return context
'''

def HomePageView(request):
	names = object.__class__.name__
	return HttpResponse(context)
