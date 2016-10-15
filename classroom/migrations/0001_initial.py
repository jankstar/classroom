# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 19:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dozent',
            fields=[
                ('id_dozent', models.AutoField(primary_key=True, serialize=False)),
                ('von', models.DateField(auto_now=True, help_text='Dozent ist verf\x9fügbar von/bis')),
                ('bis', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('id_kunde', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('01', 'aktiv'), ('02', 'inaktiv'), ('09', 'löschen')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id_kurs', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('beschreibung', models.TextField()),
                ('dauer', models.IntegerField(help_text='Dauer in Stunden')),
                ('status', models.CharField(choices=[('01', 'Inhalte planen'), ('02', 'Dozenten planen'), ('03', 'Termine planen'), ('04', 'Kurs bestät\x8aigt/l\x8aäuft'), ('09', 'Kurs beendet')], max_length=2)),
                ('id_dozent', models.ManyToManyField(to='classroom.Dozent')),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
            ],
        ),
        migrations.CreateModel(
            name='Kursinhalt',
            fields=[
                ('id_kursinhalt', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('beschreibung', models.TextField()),
                ('unterlage', models.URLField(help_text='Verzeichnis und Unterlage')),
                ('termin', models.DateTimeField(help_text='Termin zur Fertigstellung der druckfertigen Unterlagen')),
                ('status', models.CharField(choices=[('01', 'Kursinhalt planen'), ('02', 'Unterlagen druckfertig')], max_length=2)),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
            ],
        ),
        migrations.CreateModel(
            name='Kurstermin',
            fields=[
                ('id_kurstermin', models.AutoField(primary_key=True, serialize=False)),
                ('von', models.DateTimeField()),
                ('bis', models.DateTimeField()),
                ('status', models.CharField(choices=[('01', 'Termin planen'), ('02', 'Termin geplant'), ('03', 'Termin best\x8atigt'), ('09', 'Termin durchgef\x9fhrt')], max_length=2)),
                ('id_dozent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Dozent')),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
                ('id_kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kurs')),
            ],
        ),
        migrations.CreateModel(
            name='Raum',
            fields=[
                ('id_raum', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('von', models.DateField(help_text='Raum verfü\x9fgbar ab')),
                ('bis', models.DateField(help_text='Raum verf\x9fügbar bis')),
                ('bemerkung', models.TextField()),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
            ],
        ),
        migrations.CreateModel(
            name='Schulung',
            fields=[
                ('id_schulung', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('version', models.IntegerField(default=1)),
                ('beschreibung', models.TextField()),
                ('start', models.DateField()),
                ('ende', models.DateField()),
                ('status', models.CharField(choices=[('01', 'Kurse planen'), ('02', 'Termine planen'), ('03', 'Schulung best\x8aäigt/lä\x8auft'), ('09', 'Schulung beendet')], max_length=2)),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
            ],
        ),
        migrations.CreateModel(
            name='Standort',
            fields=[
                ('id_standort', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('ort', models.CharField(max_length=40)),
                ('plz', models.IntegerField()),
                ('strasse', models.CharField(max_length=40)),
                ('telefon1', models.CharField(max_length=40)),
                ('telefon2', models.CharField(max_length=40)),
                ('bemerkung', models.TextField()),
                ('id_ansprechpartner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
            ],
        ),
        migrations.CreateModel(
            name='Teilnehmer',
            fields=[
                ('id_teilnehmer', models.AutoField(primary_key=True, serialize=False)),
                ('von', models.DateField(auto_now=True, help_text='Teilnehmer ist verfü\x9fgbar von/bis')),
                ('bis', models.DateField()),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teilnehmergruppe',
            fields=[
                ('id_teilnehmergruppe', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('id_kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde')),
                ('id_teilnehmer', models.ManyToManyField(to='classroom.Teilnehmer')),
            ],
        ),
        migrations.AddField(
            model_name='raum',
            name='id_standort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Standort'),
        ),
        migrations.AddField(
            model_name='kurstermin',
            name='id_raum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Raum'),
        ),
        migrations.AddField(
            model_name='kurstermin',
            name='id_schulung',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Schulung'),
        ),
        migrations.AddField(
            model_name='kursinhalt',
            name='id_schulung',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Schulung'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='id_raumauswahl',
            field=models.ManyToManyField(to='classroom.Raum'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='id_schulung',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Schulung'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='id_teilnehmergruppe',
            field=models.ManyToManyField(to='classroom.Teilnehmergruppe'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='id_vorkurs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kurs'),
        ),
        migrations.AddField(
            model_name='dozent',
            name='id_kunde',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Kunde'),
        ),
        migrations.AddField(
            model_name='dozent',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]