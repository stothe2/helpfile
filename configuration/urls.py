from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from configuration import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<apmcontrols_id>\d+)/$', views.detail, name='detail')
)

urlpatterns += staticfiles_urlpatterns()
