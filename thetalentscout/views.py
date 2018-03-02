# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from thetalentscout.models import Giocatore, Categoria, Gara, Giocatoregara, Giudizio, Fotogiocatoregara, Conduzione
from thetalentscout.models import Recuperapalla, Controllo, Calciare, Fisicita, Giocoditesta, Marcatura, Smarcamento
from thetalentscout.models import Struttura, Giudizio
from django.shortcuts import redirect
from .forms import GiocatoreForm, ItemForm, GaraForm, FotogiocatoregaraForm, ConduzioneForm, ControlloForm
from .forms import StrutturaForm, CategoriaForm, GiocatoregaraForm, RecuperaPallaForm, CalciareForm
from .forms import FisicitaForm, GiocoditestaForm, MarcaturaForm, SmarcamentoForm, StrutturaForm, GiudizioForm
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.template.context import RequestContext, Context
import simplejson
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import xlwt

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.lib.utils import ImageReader

# class IndexView(generic.ListView):
#     template_name = 'thetalentscout/index.html'
#     context_object_name = 'lista_giocatori'
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(IndexView, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['lista_giocatori'] = Giocatore.objects.all()
#         return context


class IndexView(generic.ListView):
    template_name = 'thetalentscout/index.html'
    context_object_name = 'lista_giocatori'

    def get_queryset(self):
        if self.request.user.is_active:
            query = self.request.GET.get('search_box')
            valoreAgenzia = self.request.GET.get('sele1')
            id_utente = self.request.user.id
            anno = self.request.GET.get('id_anno')
            if anno == None or anno == '':
                daadata = '1950-01-01'
                adata = '2100-12-31'
            else:
                daadata = anno + '-01-01'
                adata = anno + '-12-31'

            if valoreAgenzia == None:
                valoreAgenzia = '1'

            if valoreAgenzia <> '1' :
                agenzia = "Talent"

            if self.request.user.first_name == "SCOUT":
                queryset_giocatori = Giocatore.objects.filter(utente=id_utente).filter(datanascita__range=(daadata, adata)).order_by('cognome', 'nome')
            else:
                queryset_giocatori = Giocatore.objects.filter(datanascita__range=(daadata, adata)).order_by('cognome', 'nome')

            if query:
                if valoreAgenzia == '1':
                    queryset_giocatori = queryset_giocatori.filter(cognome__contains=query).order_by('cognome', 'nome')
                if valoreAgenzia == '2':
                    queryset_giocatori = queryset_giocatori.filter(agente__iexact=agenzia).filter(cognome__contains=query).order_by('cognome', 'nome')
                if valoreAgenzia == '3':
                    queryset_giocatori = queryset_giocatori.exclude(agente__contains=agenzia).filter(cognome__contains=query).order_by('cognome', 'nome')
            else:
                if valoreAgenzia == '1':
                    queryset_giocatori = queryset_giocatori.all().order_by('cognome', 'nome')
                if valoreAgenzia == '2':
                    queryset_giocatori = queryset_giocatori.filter(agente__iexact=agenzia).order_by('cognome', 'nome')
                if valoreAgenzia == '3':
                    queryset_giocatori = queryset_giocatori.exclude(agente__contains=agenzia).order_by('cognome', 'nome')

            return (queryset_giocatori)
        else:
            return HttpResponse('non sei loggato')

class ListaGiocatoriView(generic.ListView):
    template_name = 'thetalentscout/lista_giocatori.html'
    context_object_name = 'lista_giocatori'

    def get_queryset(self):
        id_utente = self.request.user.id
        if self.request.user.first_name == "SCOUT":
            queryset_giocatori = Giocatore.objects.filter(utente=id_utente).order_by('cognome', 'nome')
        else:
            queryset_giocatori = Giocatore.objects.all().order_by('cognome', 'nome')

        query = self.request.GET.get('search_box')
        if query:
            return queryset_giocatori.filter(cognome__contains=query).order_by('cognome', 'nome')
        else:
            return queryset_giocatori.all()


class ListaGareView(generic.ListView):
    template_name = 'thetalentscout/lista_gare.html'
    context_object_name = 'lista_gare'

    def get_queryset(self):
        """Return the last five published questions."""
        return Gara.objects.order_by('-datainserimento','categoria__desccategoria')

def lista_partite(request):
    if request.user.is_active:
        id_categoriascelta = request.GET.get('id_categoria')
        id_annoscelto = request.GET.get('id_anno')
        cat_scelta = ""
        categ_sel = ""

        if id_categoriascelta == None  or id_categoriascelta == 'Z':
            if id_annoscelto == None or id_annoscelto == 'Z':
                lista_gare = Gara.objects.order_by('-dataincontro', 'categoria__desccategoria')
            else:
                #è stato scelto solo l'anno
                da_data = id_annoscelto + "-" + "01-01"
                a_data = id_annoscelto + "-" + "12-31"
                lista_gare = Gara.objects.filter(dataincontro__range=(da_data,a_data)).order_by('-dataincontro', 'categoria__desccategoria')
        else:
            if id_annoscelto == None or id_annoscelto == 'Z':
                lista_gare = Gara.objects.filter(categoria=id_categoriascelta).order_by('-dataincontro')
                cat_scelta = Categoria.objects.filter(id=id_categoriascelta)
                for s in cat_scelta:
                    categ_sel = s.desccategoria
            else:
                # è stato scelto solo l'anno
                da_data = id_annoscelto + "-" + "01-01"
                a_data = id_annoscelto + "-" + "12-31"
                lista_gare = Gara.objects.filter(categoria=id_categoriascelta, dataincontro__range=(da_data, a_data)).order_by('-dataincontro')
                cat_scelta = Categoria.objects.filter(id=id_categoriascelta)
                for s in cat_scelta:
                    categ_sel = s.desccategoria


        categ = Categoria.objects.all().order_by('desccategoria')
        #cerco gli anni delle partite inserite
        anni_partite = []
        #distinct degli anni su tabella Gare ordinata per anni decrescente
        distinct_anni = Gara.objects.all().order_by('-dataincontro')
        anno_old = ""
        for s in distinct_anni:
            date_string = s.dataincontro.strftime('%Y')
            if anno_old <> date_string:
                anni_partite.append({'anno': date_string})
                anno_old = date_string

    return render(request, 'thetalentscout/lista_partite.html', {'lista_gare': lista_gare , \
                                                                 'categ': categ, \
                                                                 'anni_partite':  anni_partite, \
                                                                 'annoselezionato': id_annoscelto, \
                                                                 'catselezionata': id_categoriascelta, \
                                                                 'desccatscelta': categ_sel})

def new_giocatore(request):
    if request.method == "POST":
        form = GiocatoreForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.utente = request.user
            post.save()
            return HttpResponseRedirect('../../../thetalentscout/giocatori')
    else:
        form = GiocatoreForm()
    return render(request, 'thetalentscout/inserisci_giocatore.html', {'form': form})

def modificagiocatore(request,idc):
    posts = Giocatore.objects.filter(id=idc)
    #posts = Giocatore.objects.all()
    return render( request, "thetalentscout/modifica_giocatore.html", {'posts': posts})

def new_struttura(request):
    if request.method == "POST":
        form = StrutturaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('../../../thetalentscout/struttura')
    else:
        form = StrutturaForm()
    return render(request, 'thetalentscout/inserisci_struttura.html', {'form': form})

def new_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.desccategoria)
            primalettera = post.desccategoria[:1]
            inizio = primalettera.upper()
            resto = post.desccategoria[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Categoria.objects.filter(desccategoria=str_descr).count()
            if (num_descr == 0):
                post.desccategoria = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/categoria')
    else:
        form = CategoriaForm()
        lista_descr = Categoria.objects.all().order_by('desccategoria')
    return render(request, 'thetalentscout/categoria.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_conduzione(request):
    if request.method == "POST":
        form = ConduzioneForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descconduzione)
            primalettera = post.descconduzione[:1]
            inizio = primalettera.upper()
            resto = post.descconduzione[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Conduzione.objects.filter(descconduzione=str_descr).count()
            if (num_descr == 0):
                post.descconduzione = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/conduzione')
    else:
        form = ConduzioneForm()
        lista_descr = Conduzione.objects.all().order_by('descconduzione')
    return render(request, 'thetalentscout/conduzione.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_calciare(request):
    if request.method == "POST":
        form = CalciareForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.desccalciare)
            primalettera = post.desccalciare[:1]
            inizio = primalettera.upper()
            resto = post.desccalciare[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Calciare.objects.filter(desccalciare=str_descr).count()
            if (num_descr == 0):
                post.desccalciare = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/calciare')
    else:
        form = CalciareForm()
        lista_descr = Calciare.objects.all().order_by('desccalciare')
    return render(request, 'thetalentscout/calciare.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_controllo(request):
    if request.method == "POST":
        form = ControlloForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.desccontrollo)
            primalettera = post.desccontrollo[:1]
            inizio = primalettera.upper()
            resto = post.desccontrollo[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Controllo.objects.filter(desccontrollo=str_descr).count()
            if (num_descr == 0):
                post.desccontrollo = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/controllo')
    else:
        form = ControlloForm()
        lista_descr = Controllo.objects.all().order_by('desccontrollo')
    return render(request, 'thetalentscout/controllo.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_fisicita(request):
    if request.method == "POST":
        form = FisicitaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descfisicita)
            primalettera = post.descfisicita[:1]
            inizio = primalettera.upper()
            resto = post.descfisicita[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Fisicita.objects.filter(descfisicita=str_descr).count()
            if (num_descr == 0):
                post.descfisicita = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/fisicita')
    else:
        form = FisicitaForm()
        lista_descr = Fisicita.objects.all().order_by('descfisicita')
    return render(request, 'thetalentscout/fisicita.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_giocoditesta(request):
    if request.method == "POST":
        form = GiocoditestaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descgiocoditesta)
            primalettera = post.descgiocoditesta[:1]
            inizio = primalettera.upper()
            resto = post.descgiocoditesta[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Giocoditesta.objects.filter(descgiocoditesta=str_descr).count()
            if (num_descr == 0):
                post.descgiocoditesta = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/giocoditesta')
    else:
        form = GiocoditestaForm()
        lista_descr = Giocoditesta.objects.all().order_by('descgiocoditesta')
    return render(request, 'thetalentscout/giocoditesta.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_marcatura(request):
    if request.method == "POST":
        form = MarcaturaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descmarcatura)
            primalettera = post.descmarcatura[:1]
            inizio = primalettera.upper()
            resto = post.descmarcatura[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Marcatura.objects.filter(descmarcatura=str_descr).count()
            if (num_descr == 0):
                post.descmarcatura = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/marcatura')
    else:
        form = MarcaturaForm()
        lista_descr = Marcatura.objects.all().order_by('descmarcatura')
    return render(request, 'thetalentscout/marcatura.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_smarcamento(request):
    if request.method == "POST":
        form = SmarcamentoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descsmarcamento)
            primalettera = post.descsmarcamento[:1]
            inizio = primalettera.upper()
            resto = post.descsmarcamento[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Smarcamento.objects.filter(descsmarcamento=str_descr).count()
            if (num_descr == 0):
                post.descsmarcamento = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/marcamento')
    else:
        form = SmarcamentoForm()
        lista_descr = Smarcamento.objects.all().order_by('descsmarcamento')
    return render(request, 'thetalentscout/smarcamento.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_struttura(request):
    if request.method == "POST":
        form = StrutturaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descstruttura)
            primalettera = post.descstruttura[:1]
            inizio = primalettera.upper()
            resto = post.descstruttura[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Struttura.objects.filter(descstruttura=str_descr).count()
            if (num_descr == 0):
                post.descstruttura = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/struttura')
    else:
        form = StrutturaForm()
        lista_descr = Struttura.objects.all().order_by('descstruttura')
    return render(request, 'thetalentscout/struttura.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_giudizio(request):
    if request.method == "POST":
        form = GiudizioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descgiudizio)
            primalettera = post.descgiudizio[:1]
            inizio = primalettera.upper()
            resto = post.descgiudizio[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Giudizio.objects.filter(descgiudizio=str_descr).count()
            if (num_descr == 0):
                post.descgiudizio = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/giudizio')
    else:
        form = GiudizioForm()
        lista_descr = Giudizio.objects.all().order_by('descgiudizio')
    return render(request, 'thetalentscout/giudizio.html', {'form': form, \
                                                              'lista_descr': lista_descr})

def new_recuperapalla(request):
    if request.method == "POST":
        form = RecuperaPallaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lungparola = len(post.descrecuperapalla)
            primalettera = post.descrecuperapalla[:1]
            inizio = primalettera.upper()
            resto = post.descrecuperapalla[1:lungparola]
            fine = resto.lower()
            str_descr = inizio + fine
            num_descr = Recuperapalla.objects.filter(descrecuperapalla=str_descr).count()
            if (num_descr == 0):
                post.descrecuperapalla = str_descr
                post.save()
            return HttpResponseRedirect('../../../thetalentscout/recuperapalla')
    else:
        form = RecuperaPallaForm()
        lista_descr = Recuperapalla.objects.all().order_by('descrecuperapalla')
    return render(request, 'thetalentscout/recuperapalla.html', {'form': form, \
                                                              'lista_descr': lista_descr})


def gare_del_giocatore(request,idc):
    distinctgarevisionate = Giocatoregara.objects.filter(giocatore=idc).values_list('gara',flat = True).distinct()
    datigarevisionate = Gara.objects.filter(id__in=distinctgarevisionate).order_by('-dataincontro')

    posts = Giocatoregara.objects.filter(giocatore=idc).order_by('-datainserimento')
    conta = posts.count()   #quante volte il giocatore è stato visionato
    anagrafica = Giocatore.objects.filter(id=idc)

    #per ogni gara visionata prendo i dettagli di gara-giocatore
    dettagli = []
    for garavisionata in datigarevisionate:
        dettagliogara = Giocatoregara.objects.filter(giocatore=idc).filter(gara=garavisionata.id)
        dataold = ""
        for dettaglio in dettagliogara:
            if dataold == dettaglio.gara.dataincontro:
                dettaglio.gara.dataincontro = " "
            else:
                dataold = dettaglio.gara.dataincontro
            dettagli.append({'dettaglio': dettaglio})

    giudizi = []
    # lista dei giudizi
    pergiudizio = Giocatoregara.objects.filter(giocatore=idc).order_by('giudizio')
    #per ogni giudizio devo vedere le volte
    old_s = ""
    for s in pergiudizio:
        numeratore = Giocatoregara.objects.filter(giocatore=idc, giudizio=s.giudizio).count()
        if s.giudizio <> old_s:
            giudizi.append({'numerovolte': numeratore, 'descriz': s.giudizio})
        old_s = s.giudizio

    return render( request, "thetalentscout/gare_del_giocatore.html", {'posts': posts , \
                                                                       'conta': conta , \
                                                                       'giudizi': giudizi, \
                                                                       'anagrafica': anagrafica, \
                                                                       'dettagli': dettagli})

def dettaglio_gara_giocatore(request,idc,idg):
    posts = Giocatoregara.objects.filter(giocatore=idc, gara=idg)
    gara = Gara.objects.filter(id=idg)
    return render( request, "thetalentscout/dettaglio_gara_giocatore.html", {'posts': posts, \
                                                                             'gara': gara, \
                                                                              'idc': idc})


def mod_calciatore(request,idc):
    giocat = Giocatore.objects.get(id=idc)
    form = ItemForm(instance=giocat)
    data = {}
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=giocat)
        if not form.is_valid():
            data['form'] = form
            return render_to_response('thetalentscout/modifica_giocatore.html', data, request)

        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect('../../../thetalentscout/giocatori')
    else:
        return render(request, 'thetalentscout/modifica_giocatore.html', {'form': form, \
                                                                          'giocat': giocat})


def new_gara(request,str_tipo):
    data = {}
    if request.method == "POST":
        form = GaraForm(request.POST)
        if not form.is_valid():
            data['form'] = form
            return render_to_response('thetalentscout/inserisci_gara.html', data, request)
        post = form.save(commit=False)
        post.utente = request.user
        post.save()
        return HttpResponseRedirect('../../../thetalentscout/giocatori')
    else:
        form = GaraForm(initial={'tipo': str_tipo})
    return render(request, 'thetalentscout/inserisci_gara.html', {'form': form,
                                                                  'str_tipo': str_tipo})

def new_gara_amichevole(request,str_tipo):
    data = {}
    if request.method == "POST":
        form = GaraForm(request.POST)
        if not form.is_valid():
            data['form'] = form
            return render_to_response('thetalentscout/inserisci_gara_amichevole.html', data, request)
        post = form.save(commit=False)
        post.utente = request.user
        post.save()
        return HttpResponseRedirect('../../../thetalentscout/giocatori')
    else:
        form = GaraForm(initial={'tipo': str_tipo})

    return render(request, 'thetalentscout/inserisci_gara_amichevole.html', {'form': form,
                                                                             'str_tipo': str_tipo})

def new_gara_raduno(request,str_tipo):
    data = {}
    if request.method == "POST":
        form = GaraForm(request.POST)
        if not form.is_valid():
            data['form'] = form
            return render_to_response('thetalentscout/inserisci_gara_raduno.html', data, request)
        post = form.save(commit=False)
        post.utente = request.user
        post.save()
        return HttpResponseRedirect('../../../thetalentscout/giocatori')
    else:
        form = GaraForm(initial={'tipo': str_tipo})
    return render(request, 'thetalentscout/inserisci_gara_raduno.html', {'form': form,
                                                                         'str_tipo': str_tipo})

def mod_gara(request,idg):
    partita = Gara.objects.get(id=idg)
    form = GaraForm(instance=partita)
    data = {}
    if request.method == "POST":
        form = GaraForm(request.POST, instance=partita )
        if not form.is_valid():
            data['form'] = form
            return render_to_response('thetalentscout/modifica_gara.html', data, request)
        post = form.save(commit=False)
        post.utente = request.user
        post.save()
        return HttpResponseRedirect('../../../gara/lista')
    else:
        if partita.tipo == 'U':
            return render(request, 'thetalentscout/modifica_gara.html', {'form': form})
        else:
            if partita.tipo == 'A':
                return render(request, 'thetalentscout/modifica_gara_amichevole.html', {'form': form})
            else:
                if partita.tipo == 'R':
                    return render(request, 'thetalentscout/modifica_gara_raduno.html', {'form': form})

def dettaglio_gara_giocatore(request,idc,idg):
    posts = Giocatoregara.objects.filter(giocatore=idc, gara=idg)
    gara = Gara.objects.filter(id=idg)
    return render( request, "thetalentscout/dettaglio_gara_giocatore.html", {'posts': posts, \
                                                                             'gara': gara, \
                                                                              'idc': idc})
def modifica_gara_giocatore(request,idc,idg):
    partita = Giocatoregara.objects.get(gara=idg, giocatore=idc)
    form = GiocatoregaraForm(instance=partita)
    anagrafica = Giocatore.objects.filter(id=idc)
    gara = Gara.objects.filter(id=idg)

    if request.method == "POST":
        form = GiocatoregaraForm(request.POST, instance=partita)
        if form.is_valid():
            post = form.save(commit=False)
            post.utente = request.user
            post.save()
            return HttpResponseRedirect('../../%s' % idc)


    return render(request, 'thetalentscout/modifica_gara_giocatore.html', {'form': form, \
                                                                           'anagrafica': anagrafica, \
                                                                           'gara': gara, \
                                                                           'idc': idc, \
                                                                           'visionato': partita.utente})

def new_gara_giocatore(request,idc):
    if request.method == "POST":
        form = GiocatoregaraForm(request.POST)
        idcalciatore = request.POST['idcalciatore']
        partitascelta = request.POST['id_partita']

        # categoria = request.POST['id_categoria']
        # datascelta = partitascelta[:10]
        # date_string = datascelta[-4:] + "-" + datascelta[3:5] + "-" + datascelta[:2]
        # partitascelta = partitascelta[11:]
        # trattino = partitascelta.index("-")
        # duepunti = partitascelta.index(":")
        # squadrainscelta = partitascelta[:trattino-1]
        # squadraoutscelta = partitascelta[trattino+2:duepunti]

        # datigarascelta = Gara.objects.filter(categoria=categoria, squadrain=squadrainscelta, \
        #                                      squadraout=squadraoutscelta, dataincontro=date_string)

        spartitascelta = str(partitascelta)[-6:]
        ipartitascelta = int(spartitascelta)
        datigarascelta = Gara.objects.filter(id=ipartitascelta)

        for gara in datigarascelta:
            idgara = gara.id

        if form.is_valid():
            post = form.save(commit=False)
            post.gara_id = idgara
            post.giocatore_id = idcalciatore
            post.utente = request.user
            post.save()
            return HttpResponseRedirect('../../../giocatore/gare/%s' % idcalciatore)
            #return HttpResponseRedirect('../../../..')
    else:
        anagrafica = Giocatore.objects.filter(id=idc)
        categ = Categoria.objects.all().order_by('desccategoria')
        gare = Gara.objects.all()
        form = GiocatoregaraForm()
    return render(request, 'thetalentscout/inserisci_gara_giocatore.html', {'form': form, \
                                                                            'anagrafica': anagrafica, \
                                                                            'categ': categ, \
                                                                            'gare': gare})

class getpartitepercategoria(View):

    def get(self, request, *args, **kwargs):

        idcategoria = request.GET['id_categoria']
        listapartitepercategoria = Gara.objects.filter(categoria=idcategoria).order_by('-dataincontro', 'squadrain', 'squadraout')
        listapartite_dict = {}
        listaidpartite_dict = {}
        i=1
        for gara in listapartitepercategoria:
            date_string = gara.dataincontro.strftime('%d/%m/%Y')
            partita = date_string + " " + gara.squadrain + " - " + gara.squadraout + ": " + gara.risultato
            numpartita = gara.id
            snumpartita = "00000" + str(numpartita)
            snumpartita = snumpartita[-6:]
            snumpartita = str(i) + snumpartita
            inumpartita = int(snumpartita)
            listapartite_dict[inumpartita] = partita
            i=i+1

        return HttpResponse(simplejson.dumps(listapartite_dict, sort_keys=False), content_type="application/json")
    # def get(self, request, *args, **kwargs):
    #
    #     idcategoria = request.GET['id_categoria']
    #     listapartitepercategoria = Gara.objects.filter(categoria=idcategoria).order_by('-dataincontro', 'squadrain', 'squadraout')
    #     listapartite_dict = {}
    #     listaidpartite_dict = {}
    #     i=0
    #     for gara in listapartitepercategoria:
    #         date_string = gara.dataincontro.strftime('%d/%m/%Y')
    #         partita = date_string + " " + gara.squadrain + " - " + gara.squadraout + ": " + gara.risultato
    #         listapartite_dict[i] = partita
    #         i=i+1
    #
    #     return HttpResponse(simplejson.dumps(listapartite_dict, sort_keys=False), content_type="application/json")


def foto_giocatore_gara(request, idc, idg):
    data = {}
    if request.method == "POST":
        form = FotogiocatoregaraForm(request.POST, request.FILES)
        if not form.is_valid():
             data['form'] = form
             return render_to_response('thetalentscout/modifica_giocatore.html', data, request)
        if request.FILES.__len__() > 0:
            post = form.save(commit=False)
            post.giocatore_id = idc
            post.gara_id = idg
            post.utente = request.user
            post.save()
        # Redirect to the document list after POST
        fotogiocatoregara = Fotogiocatoregara.objects.filter(giocatore_id=idc, gara_id=idg)
        return render(request, 'thetalentscout/foto_giocatore_gara.html', {'fotogiocatoregara': fotogiocatoregara, \
                                                                           'form': form})
        #return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = FotogiocatoregaraForm()
        # form = FotogiocatoregaraForm(initial={'giocatore': idc,
        #                                       'gara': idg})

        # Load documents for the list page
    #documents = Fotogiocatoregara.objects.all()
        fotogiocatoregara = Fotogiocatoregara.objects.filter(giocatore_id=idc, gara_id=idg)


    return render(request, 'thetalentscout/foto_giocatore_gara.html', {'fotogiocatoregara': fotogiocatoregara, \
                                                                       'form': form})

def new_giocatoredaformazione(request, str_cognome, str_nome, idg):
    if request.method == "POST":
        form = GiocatoreForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.utente = request.user
            post.save()
            return HttpResponseRedirect('../../../../gara/lista/modifica/%s' % idg)
    else:
        #devo controllare se giocatore è già presente
        if str_cognome == 'None':
            form = GiocatoreForm()
        else:
            if str_nome == 'None':
                form = GiocatoreForm(
                    initial={'cognome': str_cognome})
            else:
                form = GiocatoreForm(
                    initial={'cognome': str_cognome,
                             'nome': str_nome})

    return render(request, 'thetalentscout/inserisci_giocatore_da_formazione.html', {'form': form , \
                                                                                     'str_cognome': str_cognome, \
                                                                                     'str_nome': str_nome})

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password aggiornata con successo!')
        else:
            messages.error(request, 'Errore nei Dati')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'registration/change_password.html', {'form': form})


#EXCEL
def export_users_xls(request, idc):
    # query
    distinctgarevisionate = Giocatoregara.objects.filter(giocatore=idc).values_list('gara', flat=True).distinct()
    datigarevisionate = Gara.objects.filter(id__in=distinctgarevisionate).order_by('-dataincontro')

    posts = Giocatoregara.objects.filter(giocatore=idc).order_by('-datainserimento')
    anagrafica = Giocatore.objects.filter(id=idc)
    for row in anagrafica:
        strNome = row.cognome + " " + row.nome

    strNomeExcel = strNome + ".xls"

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + strNomeExcel

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

#scrive Cognome e Nome
    row_num = 0
    col_num = 0
    ws.write(row_num, col_num, strNome, font_style)

    columns = ['Data Incontro', 'Categoria', 'Partita', 'Giudizio', 'Struttura', 'Fisicità', 'Forza', 'Resistenza', 'Velocità', 'Rapidità', 'Agilità', 'Coordinazione',]
    row_num += 1
# scrive le intestazioni delle colonne
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # per ogni gara visionata prendo i dettagli di gara-giocatore
    dettagli = []
    for garavisionata in datigarevisionate:
        dettagliogara = Giocatoregara.objects.filter(giocatore=idc).filter(gara=garavisionata.id)
        dataold = ""
        for dettaglio in dettagliogara:
            col_num = 0
            row_num += 1
            if dataold == dettaglio.gara.dataincontro:
                datastr = " "
            else:
                dataold = dettaglio.gara.dataincontro
                datastr = dettaglio.gara.dataincontro.strftime('%d/%m/%Y')

            ws.write(row_num, col_num, datastr, font_style)
            col_num += 1
            ws.write(row_num, col_num, dettaglio.gara.categoria.desccategoria, font_style)
            col_num += 1
            str_incontro = dettaglio.gara.squadrain + " " + dettaglio.gara.squadraout + " "  +dettaglio.gara.risultato
            ws.write(row_num, col_num, str_incontro, font_style)
            col_num += 1
            ws.write(row_num, col_num, dettaglio.giudizio.descgiudizio, font_style)
            col_num += 1
            ws.write(row_num, col_num, dettaglio.struttura.descstruttura, font_style)
            col_num += 1
            ws.write(row_num, col_num, dettaglio.fisicita.descfisicita, font_style)
            col_num += 1
            strstringa = ''
            if dettaglio.forza == True:
                strstringa = ''
            ws.write(row_num, col_num, strstringa, font_style)
            col_num += 1
            strstringa = ''
            if dettaglio.resistenza == True:
                strstringa = 'SI'
            ws.write(row_num, col_num, strstringa, font_style)
            col_num += 1
            strstringa = ''
            if dettaglio.velocita == True:
                strstringa = 'SI'
            ws.write(row_num, col_num, strstringa, font_style)
            col_num += 1
            strstringa = ''
            if dettaglio.rapidita == True:
                strstringa = 'SI'
            ws.write(row_num, col_num, strstringa, font_style)
            col_num += 1
            strstringa = ''
            if dettaglio.agilita == True:
                strstringa = 'SI'
            ws.write(row_num, col_num, strstringa, font_style)
            col_num += 1
            strstringa = ''
            if dettaglio.coordinazione == True:
                strstringa = 'SI'
            ws.write(row_num, col_num, strstringa, font_style)

    wb.save(response)
    return response

#PDF
def some_view(request, idc):
    # query
    distinctgarevisionate = Giocatoregara.objects.filter(giocatore=idc).values_list('gara', flat=True).distinct()
    datigarevisionate = Gara.objects.filter(id__in=distinctgarevisionate).order_by('-dataincontro')

    posts = Giocatoregara.objects.filter(giocatore=idc).order_by('-datainserimento')
    anagrafica = Giocatore.objects.filter(id=idc)
    for row in anagrafica:
        strNome = row.cognome + " " + row.nome

    strNomePdf = strNome + ".pdf"

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + strNomePdf

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response,pagesize=letter)

    #titolo con il nome dell'atleta
    p.setFont('Helvetica', 18)
    #posizionamento Nome
    i=750
    j=50
    p.drawString(j, i, strNome)

    # posizionamento foto
    j = 50
    for row in anagrafica:
        # aggiunge la foto se c'è
        if row.foto == None or row.foto == '':
            i = 660
            p.setFont('Helvetica', 8)
            p.drawString(j, i, "(Foto non disponibile)")
        else:
            i = 620
            logo = row.foto
            Image = ImageReader(logo)
            p.drawImage(Image, j, i, 100, 120)

    p.setFont('Helvetica', 10)

    #dati personali, affiancati alla foto
    i=710
    j=160

    strdati = "Nato a: " + row.luogonascita + " il " + row.datanascita.strftime('%d/%m/%Y')
    p.drawString(j, i, strdati)
    i -= 15
    strdati = "Società di appartenenza: " + row.societaappertenenza
    p.drawString(j, i, strdati)
    i -= 15
    strdati = "Altezza: " + row.altezza + " - Ruolo: " + row.ruolo + " - Piede: " + row.piede.descpiede
    p.drawString(j, i, strdati)
    i -= 15
    strdati = "Scadenza Contratto: " + row.scadenzacontratto.strftime('%d/%m/%Y')
    p.drawString(j, i, strdati)
    i -= 15
    strdati = "Ingaggio: " + row.ingaggio + " Agenzia: " + row.agente
    p.drawString(j, i, strdati)
    #posizionamento dettagli
    i -= 50
    j=50
    for garavisionata in datigarevisionate:
        dettagliogara = Giocatoregara.objects.filter(giocatore=idc).filter(gara=garavisionata.id)
        dataold = ""
        for dettaglio in dettagliogara:
            if dataold == dettaglio.gara.dataincontro:
                datastr = " "
            else:
                dataold = dettaglio.gara.dataincontro
                datastr = dettaglio.gara.dataincontro.strftime('%d/%m/%Y')

            datastr += " Categoria: " + dettaglio.gara.categoria.desccategoria + " - "
            datastr += dettaglio.gara.squadrain + "-" + dettaglio.gara.squadraout + "=" + dettaglio.gara.risultato
            datastr += "   Giudizio:" + dettaglio.giudizio.descgiudizio
            p.drawString(j, i, datastr)
            i-=15

    p.showPage()
    p.save()

    return response
