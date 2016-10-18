# coding=iso-8859-15
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Kunde
class Kunde(models.Model):
    id_kunde = models.AutoField(primary_key=True, verbose_name=_(u'Kunde'))
    name = models.CharField(max_length=50, verbose_name=_(u'Name'))   
    STATUS = (('01', _(u'aktiv')),
              ('02', _(u'inaktiv')),
              ('09', _(u'löschen'))) 
    status = models.CharField(max_length=2, choices=STATUS, default='01', verbose_name=_(u'Status'))
    
    class Meta:
        verbose_name = _(u'Kunde')
        verbose_name_plural = _(u'Kunden')

    def __unicode__(self):
        return str(self.id_kunde) + " - " + self.name
            
class Standort(models.Model):
    id_standort = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE, verbose_name=_(u'Kunde'))
    name = models.CharField(max_length=50, verbose_name=_(u'Name'))
    ort = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Ort'))
    plz = models.IntegerField(blank=True, null=True, verbose_name=_(u'PLZ'))
    strasse = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Straße'))
    telefon1 = models.CharField(max_length=40, blank=True, null=True,verbose_name=_(u'Telefon 1'))
    telefon2 = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Telefon 2'))
    id_ansprechpartner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name=_(u'Anpsrechpartner'))
    bemerkung = models.TextField(blank=True, null=True, verbose_name=_(u'Bemerkung'))
            
    def __unicode__(self):
        return str(self.id_standort) + ' - ' + self.name
    
    def kunde(self):
        _kunde = Kunde.objects.get(id_kunde=self.id_kunde)
        return str(_kunde.id_kunde) + _kunde.name 
    kunde.short_description = _(u'Kunde Name')
        
    def ansp_name(self):
        _user = User.objects.get(username=self.id_ansprechpartner)
        return _user.get_full_name()
    #ansp_name = property(_ansp_name)
    ansp_name.short_description = _(u'Ansp. Name')
    
    class Meta:
        verbose_name = _(u'Standort')
        verbose_name_plural = _(u'Standorte')    
    
class Raum(models.Model):    
    id_raum = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_standort = models.ForeignKey(Standort)
    name = models.CharField(max_length=50)
    von = models.DateField(help_text= _(u"Raum verfügbar ab"), blank=True, null=True)
    bis = models.DateField(help_text= _(u"Raum verfügbar bis"), blank=True, null=True)
    bemerkung = models.TextField(blank=True, null=True)
        
    class Meta:
        verbose_name = _(u'Raum')
        verbose_name_plural = _(u'Räume')

    def __unicode__(self):
        return str(self.id_raum) + " - " + self.name
        
# Schulung: es werden mehrere Kurse durchgeführt
class Schulung(models.Model):
    id_schulung = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    name =  models.CharField(max_length=50)
    version = models.IntegerField(default=1, blank=True, null=True)
    beschreibung = models.TextField(blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    ende = models.DateField(blank=True, null=True)
    STATUS = (
              ('01', _(u'Kurse planen')),
              ('02', _(u'Termine planen')),
              ('03', _(u'Schulung bestäigt/läuft')),
              ('09', _(u'Schulung beendet')))
    status = models.CharField(max_length=2, choices=STATUS, default='01')
    
    class Meta:
        verbose_name = _(u'Schulung')
        verbose_name_plural = _(u'Schulungen')

    def __unicode__(self):
        return str(self.id_schulung) + " - " + self.name
        
class Kursinhalt(models.Model):
    id_kursinhalt = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_schulung = models.ForeignKey(Schulung)
    name =  models.CharField(max_length=50)
    beschreibung = models.TextField(blank=True, null=True)
    unterlage = models.URLField(max_length=200, help_text= _(u'Verzeichnis und Unterlage'),blank=True, null=True)
    termin = models.DateField(help_text= _(u"Termin zur Fertigstellung der druckfertigen Unterlagen"), blank=True, null=True)
    STATUS = (
              ('01', _(u'Kursinhalt planen')),
              ('02', _(u'Unterlagen druckfertig')))
    status = models.CharField(max_length=2, choices=STATUS, default='01') 
   
    class Meta:
        verbose_name = _(u'Kursinhalt')
        verbose_name_plural = _(u'Kursinhalte')

    def __unicode__(self):
        return str(self.id_kursinhalt) + " - " + self.name

class Dozent(models.Model):
    id_dozent = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_user = models.ForeignKey(User)
    von = models.DateField(auto_now=True, help_text= _(u"Dozent ist verfügbar von/bis"), blank=True, null=True)
    bis = models.DateField(auto_now=False, blank=True, null=True)
    
    class Meta:
        verbose_name = _(u'Dozent')
        verbose_name_plural = _(u'Dozenten')

    def __unicode__(self):
        _user = User.objects.get_by_natural_key(self.id_user)
        return str(self.id_dozent) + " - " + _user.lastname + ", " + _user.firstname

class Teilnehmer(models.Model):
    id_teilnehmer = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_user = models.ForeignKey(User)
    von = models.DateField(auto_now=True, help_text= _(u"Teilnehmer ist verfügbar von/bis"), blank=True, null=True)
    bis = models.DateField(auto_now=False, blank=True, null=True)
    
    class Meta:
        verbose_name = _(u'Teilnehmer')
        verbose_name_plural = _(u'Teilnehmer')

    def __unicode__(self):
        _user = User.objects.get_by_natural_key(self.id_user)
        return str(self.id_teilnehmer) + " - " + _user.lastname 

class Teilnehmergruppe(models.Model):
    id_teilnehmergruppe = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    name = models.CharField(max_length=25)
    id_teilnehmer = models.ManyToManyField(Teilnehmer)
    
    class Meta:
        verbose_name = _(u'Teilnehmergruppe')
        verbose_name_plural = _(u'Teilnehmergruppen')

    def __unicode__(self):
        return str(self.id_teilnehmergruppe) + " - " + self.name 

class Kurs(models.Model):
    id_kurs = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_schulung = models.ForeignKey(Schulung)
    name =  models.CharField(max_length=25)
    beschreibung = models.TextField(blank=True, null=True)
    id_kursinhalt = models.ManyToManyField(Kursinhalt)
    id_dozent = models.ManyToManyField(Dozent)
    id_teilnehmergruppe = models.ManyToManyField(Teilnehmergruppe)
    id_raumauswahl = models.ManyToManyField(Raum)
    dauer = models.IntegerField(help_text= _(u"Dauer in Stunden"), blank=True, null=True)
    id_vorkurs = models.ForeignKey('self')
    STATUS =  (
               ('01', _(u'Inhalte planen')),
               ('02', _(u'Dozenten planen')),
               ('03', _(u'Termine planen')),
               ('04', _(u'Kurs bestätigt/läuft')),
               ('09', _(u'Kurs beendet')))
    status = models.CharField(max_length=2, choices=STATUS, default='01')
    
    class Meta:
        verbose_name = _(u'Kurs')
        verbose_name_plural = _(u'Kurse')

    def __unicode__(self):
        return str(self.id_kurs) + " - " + self.name 
    
class Kurstermin(models.Model):
    id_kurstermin = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_schulung = models.ForeignKey(Schulung)
    id_kurs = models.ForeignKey(Kurs)
    id_raum = models.ForeignKey(Raum)
    id_dozent = models.ForeignKey(Dozent)
    von = models.DateTimeField(blank=True, null=True)
    bis = models.DateTimeField(blank=True, null=True)
    STATUS = (
              ('01', _(u'Termin planen')),
              ('02', _(u'Termin geplant')),
              ('03', _(u'Termin bestätigt')),
              ('09', _(u'Termin durchgeführt')))
    status = models.CharField(max_length=2, choices=STATUS, default='01')

    class Meta:
        verbose_name = _(u'Kurstermin')
        verbose_name_plural = _(u'Kurstermine')

    def __unicode__(self):
        return str(self.id_kurstermin) + " - " + self.name 
