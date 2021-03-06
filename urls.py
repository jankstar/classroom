from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
#from django.contrib import databrowse
from django.contrib.auth.views import login as auth_login
#from classroom.models import Kunde, Standort, Raum

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^classroom/', include('classroom.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # URL fuer databrowse
    #(r'^db/(.*)', login_required(databrowse.site.root)),
    
    # URL Login
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': './templates/login.html'}),
    url(r'^accounts/login/$', auth_login),
]

#databrowse.site.register(Kunde, Standort, Raum)