# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Piede(models.Model):
    DESCPIEDE = (
        ('Dx'),
        ('Sx')
    )
    descpiede = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descpiede

#def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#    return 'user_{0}/{1}'.format(instance.user.id, filename)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '' "%s%s/%s" %(instance.cognome, instance.nome, filename)

def salva_foto_giocatore_gara(instance, filename):

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    instance.giocatore.cognome
    instance.giocatore.nome
    instance.gara.dataincontro
    return '' "%s%s/%s/%s" %(instance.giocatore.cognome,instance.giocatore.nome,instance.gara.dataincontro, filename)

class Giocatore(models.Model):
    cognome = models.CharField(max_length=200,default=None)
    nome = models.CharField(max_length=20,default=None, blank=True, null=True)
    datanascita =  models.DateField(default=timezone.now)
    luogonascita = models.CharField(max_length=50,default=None, blank=True, null=True)
    ruolo = models.CharField(max_length=50,default=None, blank=True, null=True)
    foto = models.ImageField(upload_to=user_directory_path, default=None, blank=True, null=True)
    #foto = models.ImageField(upload_to='', default=None, blank=True, null=True)
    telefonogenitore = models.CharField(max_length=50,default=None, blank=True, null=True)
    telefonogiocatore = models.CharField(max_length=50,default=None, blank=True, null=True)
    altezza = models.CharField(max_length=10,default=None, blank=True, null=True)
    piede = models.ForeignKey('Piede')
    sistemaideale = models.CharField(max_length=50,default=None, blank=True, null=True)
    societaappertenenza = models.CharField(max_length=50,default=None, blank=True, null=True)
    scadenzacontratto = models.DateField(default=None, blank=True, null=True)
    agente = models.CharField(max_length=50,default=None, blank=True, null=True)
    ingaggio = models.CharField(max_length=50,default=None, blank=True, null=True)
    datainserimento = models.DateField(default=timezone.now)
    utente = models.ForeignKey('auth.User')

    def save(self, *args, **kwargs):
        strCognome = self.cognome.upper()
        strNome = self.nome.upper()
        self.cognome = strCognome
        self.nome = strNome

        if self.foto:
            image = Img.open(StringIO.StringIO(self.foto.read()))
            image.thumbnail((140, 180), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.foto = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.foto.name, 'image/jpeg',
                                              output.len, None)

        return super(Giocatore, self).save(*args, **kwargs)

    def __str__(self):

        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s'%(self.cognome, self.nome, \
                self.datanascita, self.luogonascita, self.ruolo, self.foto, \
                self.telefonogenitore, self.telefonogiocatore, self.altezza, self.piede, self.sistemaideale, \
                self.societaappertenenza, self.scadenzacontratto, self.agente, self.ingaggio, self.datainserimento, \
                self.utente.id)

class Gara(models.Model):
    tipo = models.CharField(max_length=1,default='U')
    categoria = models.ForeignKey('Categoria')
    squadrain = models.CharField(max_length=200,default=None)
    moduloin =  models.CharField(max_length=50,default=None, blank=True, null=True)
    squadraout = models.CharField(max_length=50,default=None)
    moduloout = models.CharField(max_length=50,default=None, blank=True, null=True)
    risultato = models.CharField(max_length=20,default=None)
    dataincontro = models.DateField(default=timezone.now)
    cognomein1= models.CharField(max_length=30,default=None, blank=True, null=True)
    nomein1 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein2 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein2 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein3 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein3 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein4 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein4 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein5 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein5 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein6 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein6 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein7 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein7 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein8 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein8 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein9 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein9 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein10 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein10 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein11 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein11 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein12 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein12 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein13 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein13 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein14 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein14 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein15 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein15 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein16 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein16 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein17 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein17 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein18 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein18 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein19 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein19 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein20 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein20 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein21 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein21 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein22 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein22 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein23 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein23 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein24 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein24 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomein25 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomein25 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout1 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout1 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout2 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout2 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout3 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout3 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout4 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout4 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout5 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout5 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout6 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout6 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout7 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout7 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout8 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout8 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout9 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout9 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout10 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout10 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout11 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout11 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout12 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout12 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout13 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout13 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout14 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout14 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout15 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout15 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout16 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout16 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout17 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout17 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout18 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout18 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout19 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout19 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout20 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout20 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout21 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout21 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout22 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout22 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout23 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout23 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout24 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout24 = models.CharField(max_length=30, default=None, blank=True, null=True)
    cognomeout25 = models.CharField(max_length=30, default=None, blank=True, null=True)
    nomeout25 = models.CharField(max_length=30, default=None, blank=True, null=True)
    datainserimento = models.DateField(default=timezone.now)
    utente = models.ForeignKey('auth.User')

    def save(self, *args, **kwargs):
        squadraIn = self.squadrain.upper()
        squadraOut = self.squadraout.upper()
        self.squadrain = squadraIn
        self.squadraout = squadraOut

        return super(Gara, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s'%( \
                self.tipo,self.categoria, self.squadrain, self.moduloin, \
                self.squadraout, self.moduloout, self.risultato, self.dataincontro, \
                self.datainserimento, self.utente.id,\
                self.cognomein1, self.nomein1, self.cognomein2, self.nomein2, \
                self.cognomein3, self.nomein3, self.cognomein4, self.nomein4, \
                self.cognomein5, self.nomein5, self.cognomein6, self.nomein6, \
                self.cognomein7, self.nomein7, self.cognomein8, self.nomein8, \
                self.cognomein9, self.nomein9, self.cognomein10, self.nomein10, \
                self.cognomein11, self.nomein11, self.cognomein12, self.nomein12, \
                self.cognomein13, self.nomein13, self.cognomein14, self.nomein14, \
                self.cognomein15, self.nomein15, self.cognomein16, self.nomein16, \
                self.cognomein17, self.nomein17, self.cognomein18, self.nomein18, \
                self.cognomein19, self.nomein19, self.cognomein20, self.nomein20, \
                self.cognomein21, self.nomein21, self.cognomein22, self.nomein22, \
                self.cognomein23, self.nomein23, self.cognomein24, self.nomein24, \
                self.cognomein25, self.nomein25, \
                self.cognomeout1, self.nomeout1, self.cognomeout2, self.nomeout2, \
                self.cognomeout3, self.nomeout3, self.cognomeout4, self.nomeout4, \
                self.cognomeout5, self.nomeout5, self.cognomeout6, self.nomeout6, \
                self.cognomeout7, self.nomeout7, self.cognomeout8, self.nomeout8, \
                self.cognomeout9, self.nomeout9, self.cognomeout10, self.nomeout10, \
                self.cognomeout11, self.nomeout11, self.cognomeout12, self.nomeout12, \
                self.cognomeout13, self.nomeout13, self.cognomeout14, self.nomeout14, \
                self.cognomeout15, self.nomeout15, self.cognomeout16, self.nomeout16, \
                self.cognomeout17, self.nomeout17, self.cognomeout18, self.nomeout18, \
                self.cognomeout19, self.nomeout19, self.cognomeout20, self.nomeout20, \
                self.cognomeout21, self.nomeout21, self.cognomeout22, self.nomeout22, \
                self.cognomeout23, self.nomeout23, self.cognomeout24, self.nomeout24, \
                self.cognomeout25, self.nomeout25)

class Struttura(models.Model):
    DESCSTRUTTURA = (
        ('Longilineo'),
        ('Normolineo'),
        ('Brevilineo')
    )
    descstruttura = models.CharField(max_length=200,default=None)

    def save(self, *args, **kwargs):
        descstruttura = self.descstruttura.upper()
        self.descstruttura = descstruttura

        return super(Struttura, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.descstruttura

class Conduzione(models.Model):
    DESCCONDUZIONE = (
        ('Libera'),
        ('Avversario'),
        ('Dribbla'),
        ('Finta')
    )
    descconduzione = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descconduzione

class Recuperapalla(models.Model):
    DESCRECUPERAPALLA = (
            ('Anticipo'),
            ('Intercetta'),
            ('Contrasta')
    )
    descrecuperapalla = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descrecuperapalla

class Marcatura(models.Model):
    DESCMARCATURA = (
        ('Postura'),
        ('Accorcia')
    )
    descmarcatura = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descmarcatura

class Categoria(models.Model):
    DESCCATEGORIA = (
        ('Serie A', 'Serie A'),
        ('Primavera', 'Primavera')
    )
    desccategoria = models.CharField(max_length=200, default=None)

    def save(self, *args, **kwargs):
        lungparola = len(self.desccategoria)
        primalettera = self.desccategoria[:1]
        inizio = primalettera.upper()
        resto = self.desccategoria[1:lungparola]
        fine = resto.lower()
        desccategoria = inizio + fine
        self.desccategoria = desccategoria

        return super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.desccategoria)

class Fisicita(models.Model):
    DESCFISICITA = (
        ('Robusto'),
        ('Medio'),
        ('Leggero')
    )
    descfisicita = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descfisicita

class Calciare(models.Model):
    DESCCALCIARE = (
        ('Passaggio'),
        ('Lancio'),
        ('Tiro'),
        ('Piazzato')
    )
    desccalciare = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.desccalciare

class Controllo(models.Model):
    DESCCONTROLLO = (
        ('Stop'),
        ('Orientato'),
        ('Protegge')
    )
    desccontrollo = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.desccontrollo

class Smarcamento(models.Model):
    DESCSMARCAMENTO = (
        ('Si Smarca'),
        ('Velocità'),
        ('Dentro/Fuori'),
        ('Corto/Lungo')
    )
    descsmarcamento = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descsmarcamento

class Giocoditesta(models.Model):
    DESCGIOCODITESTA = (
        ('Colpisce'),
        ('Elevazione'),
        ('Indirizza')
    )
    descgiocoditesta = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descgiocoditesta

class Giudizio(models.Model):
    DESCGIUDIZIO = (
        ('Buono'),
        ('Da Prendere'),
        ('Da Rivedere')
    )
    descgiudizio = models.CharField(max_length=200,default=None)

    def __unicode__(self):
        return self.descgiudizio

class Giocatoregara(models.Model):
    giocatore = models.ForeignKey('Giocatore')
    gara = models.ForeignKey('Gara')
    struttura = models.ForeignKey('Struttura')
    fisicita = models.ForeignKey('Fisicita')
    calciare = models.ForeignKey('Calciare')
    conduzione = models.ForeignKey('Conduzione')
    controllo = models.ForeignKey('Controllo')
    recuperapalla = models.ForeignKey('Recuperapalla')
    smarcamento = models.ForeignKey('Smarcamento')
    marcatura = models.ForeignKey('Marcatura')
    giocoditesta = models.ForeignKey('Giocoditesta')
    forza = models.BooleanField(default=False)
    resistenza = models.BooleanField(default=False)
    velocita = models.BooleanField(default=False)
    rapidita = models.BooleanField(default=False)
    agilita = models.BooleanField(default=False)
    coordinazione = models.BooleanField(default=False)
    personalita = models.BooleanField(default=False)
    concentrazione = models.BooleanField(default=False)
    temperamento = models.BooleanField(default=False)
    aggressivita = models.BooleanField(default=False)
    autocontrollo = models.BooleanField(default=False)
    disponibilita = models.BooleanField(default=False)
    assomiglia = models.CharField(max_length=50,default=None, blank=True, null=True)
    giudizio = models.ForeignKey('Giudizio')
    datainserimento = models.DateField(default=timezone.now)
    utente = models.ForeignKey('auth.User')

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % ( \
            self.giocatore.id, self.gara.id, self.struttura.id,self.fisicita.id,self.calciare.id,self.conduzione.id, \
            self.controllo.id, self.recuperapalla.id, self.smarcamento.id, self.marcatura.id, \
            self.giocoditesta.id, self.forza, self.resistenza, self.velocita, self.rapidita, self.agilita, \
            self.coordinazione, self.personalita, self.concentrazione, self.temperamento, self.aggressivita, \
            self.autocontrollo, self.disponibilita, self.assomiglia, self.giudizio.id, self.datainserimento, self.utente.id)

class Fotogiocatoregara(models.Model):

    giocatore = models.ForeignKey('Giocatore')
    gara = models.ForeignKey('Gara')
    foto = models.ImageField(upload_to=salva_foto_giocatore_gara, default=None, blank=True, null=True)
    #foto = models.ImageField(upload_to='', default=None, blank=True, null=True)
    utente = models.ForeignKey('auth.User')

    def save(self, *args, **kwargs):

        if self.foto:
            image = Img.open(StringIO.StringIO(self.foto.read()))
            # w, h = image.size
            image.thumbnail((600, 400), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=200)
            output.seek(0)
            self.foto = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.foto.name, 'image/jpeg',
                                              output.len, None)

        return super(Fotogiocatoregara, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s %s %s' % ( \
            self.giocatore.id, self.gara.id, self.foto, self.utente.id)