from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import databrowse
from apps.classroom.models import Kunde, Standort, Raum

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^classroom/', include('apps.classroom.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # URL fuer databrowse
    (r'^db/(.*)', login_required(databrowse.site.root)),
    
    # URL Login
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': './templates/login.html'}),
)

databrowse.site.register(Kunde, Standort, Raum)