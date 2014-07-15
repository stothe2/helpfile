from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views import generic

from configuration.models import APMControls, PMControls, TMControls, UIControls

# Create your views here.
def index(request):
	apmcontrols_list = APMControls.objects.all().order_by('-id')
	template = loader.get_template('configuration/index.html')
	context = RequestContext(request, {
		'apmcontrols_list': apmcontrols_list,
		})
	return HttpResponse(template.render(context))

def detail(request, apmcontrols_id):
	item = APMControls.objects.get(id=apmcontrols_id)
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
		'apmcontrols_id': apmcontrols_id,
		'item': item,
		'itemSet': itemSet,
		'countStr': countStr,
		'firstSet': firstSet,
		'itemCom': itemCom,
		'firstCom': firstCom,
		'combined': combined,
		})
	return HttpResponse(template.render(context))
