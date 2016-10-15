from django.contrib import admin
from django.contrib.auth.models import User
from .models import Kunde, Standort, Raum, Schulung, Kurstermin 
from .models import Kurs, Kursinhalt, Dozent, Teilnehmer, Teilnehmergruppe

class UserInline(admin.TabularInline):
    model = User
    extra = 1
    
class KundeInline(admin.TabularInline):
    model = Kunde
    extra = 1

class StandortAdmin(admin.ModelAdmin):
    inline = [KundeInline]    
    
class StandortInline(admin.TabularInline):
    model = Standort
    extra = 1    
    
class RaumAdmin(admin.ModelAdmin):
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
                    
admin.site.register(Kunde)
admin.site.register(Standort, StandortAdmin)
admin.site.register(Raum, RaumAdmin)
admin.site.register(Schulung, SchulungAdmin)
admin.site.register(Kursinhalt, KursinhaltAdmin)
admin.site.register(Dozent, DozentAdmin)
admin.site.register(Teilnehmer, TeilnehmerAdmin)
admin.site.register(Teilnehmergruppe, TeilnehmergruppeAdmin)
admin.site.register(Kurs, KursAdmin)
admin.site.register(Kurstermin, KursterminAdmin)