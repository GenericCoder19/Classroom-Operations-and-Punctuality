from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^report/', views.report, name='report'),
    url(r'^login_u/$', views.login_u, name='login_u'),
    url(r'^logout_u/$', views.logout_u, name='logout_u'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^archive/(?P<BLOCK>[A-Z]+)', views.archive_block, name='archive_block'),
    url(r'^archive/all/$', views.archive_all, name='archive_all'),
    url(r'^archive/(?P<day>[0-9]+)/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.archive_date, name='archive_date'),
    url(r'^delete_offence/(?P<id>[0-9]+)/$', views.delete_offence, name='delete_offence'),
    url(r'^register/$', views.register, name='register'),
]
