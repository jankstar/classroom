from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Kunde, Standort, Raum, Schulung, Kurstermin 
from .models import Kurs, Kursinhalt, Dozent, Teilnehmer, Teilnehmergruppe
#from django.template.defaultfilters import title

class MyAdminSite(admin.AdminSite):
    site_header = _(u'Schulungsmanager')

class UserInline(admin.TabularInline):
    model = User
    extra = 1

class KundeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    ordering = ['name']
        
class KundeInline(admin.TabularInline):
    model = Kunde
    extra = 1

class StandortAdmin(admin.ModelAdmin):
    search_fields = ['name', 'strasse']
    fieldsets = [
        (None,          {'fields': ['id_kunde', 'name']}),
        (_(u'Daten'),   {'fields': ['ort', 'plz', 'strasse','id_ansprechpartner', 'ansp_name', 'telefon1', 'telefon2','bemerkung']})]
    list_display = ['name', 'id_kunde', 'ort', 'plz', 'strasse', 'ansp_name']
    readonly_fields = ['ansp_name']
    ordering = ['id_kunde', 'name']
    inline = [KundeInline]
    
    def kunde_name(self,obj):
        _kunde = Kunde.objects.get(id_kunde=obj.id_kunde)
        return 'Test' #str(_kunde.id_kunde) + ' ' + _kunde.name + _(u' Status ') + _kunde.status  
    kunde_name.short_description = _(u'Kunde Name')
    
    def ansp_name(self,obj):
        _user = User.objects.get(username=obj.id_ansprechpartner)
        return _user.get_full_name() + ' / ' + _user.email
    ansp_name.short_description = _(u'Ansp. Name')
    
class StandortInline(admin.TabularInline):
    model = Standort
    extra = 1    
    
class RaumAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    inline = [KundeInline, StandortInline]    

class RaumInline(admin.TabularInline):
    model = Raum
    extra = 1

class SchulungAdmin(admin.ModelAdmin):
    inline = [KundeInline]    

class SchulungInline(admin.TabularInline):
    model = Schulung
    extra = 1    

class KursinhaltAdmin(admin.ModelAdmin):
    inline = [KundeInline,SchulungInline]    

class KursInline(admin.TabularInline):
    model = Kurs
    extra = 1
    
class DozentAdmin(admin.ModelAdmin):
    inline = [KundeInline, UserInline]

class DozentInline(admin.TabularInline):
    model = Dozent
    extra = 1

class TeilnehmerAdmin(admin.ModelAdmin):
    inline = [KundeInline, UserInline]

class TeilnehmerInline(admin.TabularInline):
    model = Teilnehmer
    extra = 1

class TeilnehmergruppeAdmin(admin.ModelAdmin):
    inline = [KundeInline, TeilnehmerInline]

class KursAdmin(admin.ModelAdmin):
    inline = [KundeInline, SchulungInline]

class KursterminAdmin(admin.ModelAdmin):
    inline = [KundeInline, SchulungInline, KursInline, RaumInline, DozentInline]
        
admin_site = MyAdminSite(name='admin')                    
admin.site.register(Kunde, KundeAdmin)
admin.site.register(Standort, StandortAdmin)
admin.site.register(Raum, RaumAdmin)
admin.site.register(Schulung, SchulungAdmin)
admin.site.register(Kursinhalt, KursinhaltAdmin)
admin.site.register(Dozent, DozentAdmin)
admin.site.register(Teilnehmer, TeilnehmerAdmin)
admin.site.register(Teilnehmergruppe, TeilnehmergruppeAdmin)
admin.site.register(Kurs, KursAdmin)
admin.site.register(Kurstermin, KursterminAdmin)