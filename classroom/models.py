# coding=iso-8859-15
from django.db import models
from django.contrib.auth.models import User

# Kunde
class Kunde(models.Model):
    id_kunde = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)   
    STATUS = (('01', u'aktiv'),
              ('02', u'inaktiv'),
              ('09', u'löschen')) 
    status = models.CharField(max_length=2, choices=STATUS)
    
    def __unicode__(self):
        return str(self.id_kunde) + " - " + self.name
    
class Standort(models.Model):
    id_standort = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    name = models.CharField(max_length=40)
    ort = models.CharField(max_length=40)
    plz = models.IntegerField()
    strasse = models.CharField(max_length=40)
    telefon1 = models.CharField(max_length=40)
    telefon2 = models.CharField(max_length=40)
    id_ansprechpartner = models.ForeignKey(User)
    bemerkung = models.TextField()
        
    def __unicode__(self):
        return self.id_standort + " - " + self.name
    
class Raum(models.Model):    
    id_raum = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_standort = models.ForeignKey(Standort)
    name = models.CharField(max_length=40)
    von = models.DateField(help_text= u"Raum verfügbar ab")
    bis = models.DateField(help_text= u"Raum verfügbar bis")
    bemerkung = models.TextField()
    
    def __unicode__(self):
        return self.id_raum + " - " + self.name
        
# Schulung: es werden mehrere Kurse durchgeführt
class Schulung(models.Model):
    id_schulung = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    name =  models.CharField(max_length=25)
    version = models.IntegerField(default=1)
    beschreibung = models.TextField()
    start = models.DateField()
    ende = models.DateField()
    STATUS = (
              ('01', u'Kurse planen'),
              ('02', u'Termine planen'),
              ('03', u'Schulung bestäigt/läuft'),
              ('09', u'Schulung beendet'))
    status = models.CharField(max_length=2, choices=STATUS)
    
    def __unicode__(self):
        return self.id_schulung + " - " + self.name
        
class Kursinhalt(models.Model):
    id_kursinhalt = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_schulung = models.ForeignKey(Schulung)
    name =  models.CharField(max_length=25)
    beschreibung = models.TextField()
    unterlage = models.URLField(max_length=200, help_text= u'Verzeichnis und Unterlage')
    termin = models.DateTimeField(help_text= u"Termin zur Fertigstellung der druckfertigen Unterlagen")
    STATUS = (
              ('01', u'Kursinhalt planen'),
              ('02', u'Unterlagen druckfertig'))
    status = models.CharField(max_length=2, choices=STATUS) 
   
    def __unicode__(self):
        return self.id_kursinhalt + " - " + self.name + " / " + self.id_kunde

class Dozent(models.Model):
    id_dozent = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_user = models.ForeignKey(User)
    von = models.DateField(auto_now=True, help_text= u"Dozent ist verfügbar von/bis" )
    bis = models.DateField(auto_now=False)
    
    def __unicode__(self):
        _user = User.objects.get_by_natural_key(self.id_user)
        return self.id_dozent + " - " + _user.lastname + " / " + self.id_kunde

class Teilnehmer(models.Model):
    id_teilnehmer = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_user = models.ForeignKey(User)
    von = models.DateField(auto_now=True, help_text= u"Teilnehmer ist verfügbar von/bis" )
    bis = models.DateField(auto_now=False)
    
    def __unicode__(self):
        _user = User.objects.get_by_natural_key(self.id_user)
        return self.id_teilnehmer + " - " + _user.lastname + " / " + self.id_kunde

class Teilnehmergruppe(models.Model):
    id_teilnehmergruppe = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    name = models.CharField(max_length=25)
    id_teilnehmer = models.ManyToManyField(Teilnehmer)
    
    def __unicode__(self):
        return self.id_teilnehmergruppe + " - " + self.name + " / " + self.id_kunde

class Kurs(models.Model):
    id_kurs = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_schulung = models.ForeignKey(Schulung)
    name =  models.CharField(max_length=25)
    beschreibung = models.TextField()
#    id_kursinhalt = models.ManyToManyField(Kursinhalt)
    id_dozent = models.ManyToManyField(Dozent)
    id_teilnehmergruppe = models.ManyToManyField(Teilnehmergruppe)
    id_raumauswahl = models.ManyToManyField(Raum)
    dauer = models.IntegerField(help_text= u"Dauer in Stunden")
    id_vorkurs = models.ForeignKey('self')
    STATUS =  (
               ('01', u'Inhalte planen'),
               ('02', u'Dozenten planen'),
               ('03', u'Termine planen'),
               ('04', u'Kurs bestätigt/läuft'),
               ('09', u'Kurs beendet'))
    status = models.CharField(max_length=2, choices=STATUS)
    
    def __unicode__(self):
        return self.id_kurs + " - " + self.name + " / " + self.id_kunde + " / " + self.status
    
class Kurstermin(models.Model):
    id_kurstermin = models.AutoField(primary_key=True)
    id_kunde = models.ForeignKey(Kunde)
    id_schulung = models.ForeignKey(Schulung)
    id_kurs = models.ForeignKey(Kurs)
    id_raum = models.ForeignKey(Raum)
    id_dozent = models.ForeignKey(Dozent)
    von = models.DateTimeField()
    bis = models.DateTimeField()
    STATUS = (
              ('01', u'Termin planen'),
              ('02', u'Termin geplant'),
              ('03', u'Termin besttigt'),
              ('09', u'Termin durchgefhrt'))
    status = models.CharField(max_length=2, choices=STATUS)

    def __unicode__(self):
        return self.id_kurstermin + " - " + self.name + " / " + self.id_kunde + " / " + self.status
