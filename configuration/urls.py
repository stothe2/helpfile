from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from configuration import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	#url(r'^controls/apm/$', views.IndexView.as_view(), name='index')
	url(r'^(?P<apm_id>\d+)/$', views.detail, name='detail')
)

urlpatterns += staticfiles_urlpatterns()
