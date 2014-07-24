from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from configuration import views

urlpatterns = patterns('',
	url(r'^$', views.generic.TemplateView.as_view(template_name='home.html')),
	url(r'^APM/$', views.APMIndexView.as_view(), name='index'),
	url(r'^PM/$', views.PMIndexView.as_view(), name='index'),
	url(r'^TM/$', views.TMIndexView.as_view(), name='index'),
	url(r'^UI/$', views.UIIndexView.as_view(), name='index'),
	url(r'^APM/(?P<pk>\d+)/$', views.APMDetailView.as_view(), name='detail'),
	url(r'^PM/(?P<pk>\d+)/$', views.PMDetailView.as_view(), name='detail'),
	url(r'^TM/(?P<pk>\d+)/$', views.TMDetailView.as_view(), name='detail'),
	url(r'^UI/(?P<pk>\d+)/$', views.UIDetailView.as_view(), name='detail'),
	url(r'^APM/table/$', views.APMTableView.as_view(), name='table'),
	url(r'^PM/table/$', views.PMTableView.as_view(), name='table'),
	url(r'^TM/table/$', views.TMTableView.as_view(), name='table'),
	url(r'^UI/table/$', views.UITableView.as_view(), name='table'),
)

urlpatterns += staticfiles_urlpatterns()
