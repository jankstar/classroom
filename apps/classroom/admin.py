from classroom.models import Kunde
from classroom.models import Standort
from django.contrib import admin


class KundeInline(admin.TabularInline):
    model = Kunde
    extra = 1

class StandortAdmin(admin.ModelAdmin):
    inlines = [KundeInline]


admin.site.register(Kunde)
admin.site.register(Standort, StandortAdmin)
