from django.conf.urls import url

from . import views
from views import getpartitepercategoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


app_name = 'thetalentscout'

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^password/$', views.change_password, name='change_password'),
    # url(r'^resetpassword/$', views.reset_password, name='reset_password'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^giocatori$', login_required(views.ListaGiocatoriView.as_view()), name='lista_giocatori'),
    url(r'^conduzione$', login_required(views.new_conduzione), name='conduzione'),
    url(r'^recuperapalla$', login_required(views.new_recuperapalla), name='recuperapalla'),
    url(r'^calciare$', login_required(views.new_calciare), name='calciare'),
    url(r'^controllo$', login_required(views.new_controllo), name='controllo'),
    url(r'^fisicita$', login_required(views.new_fisicita), name='fisicita'),
    url(r'^giocoditesta$', login_required(views.new_giocoditesta), name='giocoditesta'),
    url(r'^marcatura$', login_required(views.new_marcatura), name='marcatura'),
    url(r'^smarcamento$', login_required(views.new_smarcamento), name='smarcamento'),
    url(r'^struttura$', login_required(views.new_struttura), name='struttura'),
    url(r'^giudizio$', login_required(views.new_giudizio), name='giudizio'),
    url(r'^giocatori/inserisci/$', login_required(views.new_giocatore), name='new_giocatore'),
    url(r'^giocatori/modifica/(?P<idc>[0-9]+)$', login_required(views.mod_calciatore), name='mod_calciatore'),
    url(r'^struttura/inserisci$', login_required(views.new_struttura), name='new_struttura'),
    url(r'^categoria$', login_required(views.new_categoria), name='categoria'),
    url(r'^giocatore/gare/(?P<idc>[0-9]+)$', login_required(views.gare_del_giocatore), name='gare_del_giocatore'),
    # url(r'^giocatore/gare/(?P<idc>[0-9]+)/dettaglio/(?P<idg>[0-9]+)$', login_required(views.dettaglio_gara_giocatore), name='dettaglio_gara_giocatore'),
    url(r'^giocatore/gare/(?P<idc>[0-9]+)/dettaglio/(?P<idg>[0-9]+)$', login_required(views.modifica_gara_giocatore), name='modifica_gara_giocatore'),
    url(r'^gara/inserisci/(?P<str_tipo>.*)$', login_required(views.new_gara), name='new_gara'),
    url(r'^gara/inserisci20/(?P<str_tipo>.*)$', login_required(views.new_gara_amichevole), name='new_gara_amichevole'),
    url(r'^gara/inserisci25/(?P<str_tipo>.*)$', login_required(views.new_gara_raduno), name='new_gara_raduno'),
    # url(r'^gara/lista$', login_required(views.ListaGareView.as_view()), name='lista_gare'),
    url(r'^gara/lista$', login_required(views.lista_partite), name='lista_partite'),
    url(r'^gara/lista/modifica/(?P<idg>[0-9]+)$', login_required(views.mod_gara), name='mod_gara'),
    url(r'^giocatore/gare/new_dettaglio/(?P<idc>[0-9]+)$', login_required(views.new_gara_giocatore), name='new_gara_giocatore'),
    url(r'^giocatore/gare/foto/(?P<idc>[0-9]+)/(?P<idg>[0-9]+)$', login_required(views.foto_giocatore_gara), name='foto_giocatore_gara'),
    url(r'^giocatori/inseriscidaformazione/(?P<str_cognome>.*)/(?P<str_nome>.*)/(?P<idg>[0-9]+)$', login_required(views.new_giocatoredaformazione), name='new_giocatoredaformazione'),

# Letture
    url(r'^getgare', getpartitepercategoria.as_view(), name='getpartitepercategoria'),

# Export to Excel
    url(r'^giocatore/gare/export_xls/(?P<idc>[0-9]+)$', login_required(views.export_users_xls), name='export_users_xls'),
# Export to PDF
    url(r'^giocatore/gare/export_pdf/(?P<idc>[0-9]+)$', login_required(views.some_view), name='some_view'),

]
