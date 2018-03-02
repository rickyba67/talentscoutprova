from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Giocatore
from .models import Piede
from .models import Gara
from .models import Giocatoregara
from .models import Struttura
from .models import Conduzione
from .models import Recuperapalla
from .models import Marcatura
from .models import Categoria
from .models import Controllo
from .models import Smarcamento
from .models import Giocoditesta
from .models import Fisicita
from .models import Calciare
from .models import Fotogiocatoregara
from .models import Giudizio

class FotogiocatoregaraForm(forms.ModelForm):

    class Meta:
        model = Fotogiocatoregara
        fields = ('foto',)

class GiocatoreForm(forms.ModelForm):
    class Meta:
        model = Giocatore
        fields = (  'cognome',
                    'nome',
                    'datanascita',
                    'luogonascita',
                    'ruolo',
                    'foto',
                    'telefonogenitore',
                    'telefonogiocatore',
                    'altezza',
                    'piede',
                    'sistemaideale',
                    'societaappertenenza',
                    'scadenzacontratto',
                    'agente',
                    'ingaggio',
                    )


class StrutturaForm(forms.ModelForm):
    class Meta:
        model = Struttura
        fields = ('descstruttura',)
        labels = {  'descstruttura': _('Descrizione'),
                 }

class ConduzioneForm(forms.ModelForm):
    class Meta:
        model = Conduzione
        fields = ('descconduzione',)
        labels = {  'descconduzione': _('Descrizione'),
                 }

class RecuperaPallaForm(forms.ModelForm):
    class Meta:
        model = Recuperapalla
        fields = ('descrecuperapalla',)
        labels = {  'descrecuperapalla': _('Descrizione'),
                 }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('desccategoria',)
        labels = {  'desccategoria': _('Descrizione'),
                 }

class CalciareForm(forms.ModelForm):
    class Meta:
        model = Calciare
        fields = ('desccalciare',)
        labels = {  'desccalciare': _('Descrizione'),
                 }

class ControlloForm(forms.ModelForm):
    class Meta:
        model = Controllo
        fields = ('desccontrollo',)
        labels = {  'desccontrollo': _('Descrizione'),
                 }

class FisicitaForm(forms.ModelForm):
    class Meta:
        model = Fisicita
        fields = ('descfisicita',)
        labels = {  'descfisicita': _('Descrizione'),
                 }

class GiocoditestaForm(forms.ModelForm):
    class Meta:
        model = Giocoditesta
        fields = ('descgiocoditesta',)
        labels = {  'descgiocoditesta': _('Descrizione'),
                 }

class MarcaturaForm(forms.ModelForm):
    class Meta:
        model = Marcatura
        fields = ('descmarcatura',)
        labels = {  'descmarcatura': _('Descrizione'),
                 }

class SmarcamentoForm(forms.ModelForm):
    class Meta:
        model = Smarcamento
        fields = ('descsmarcamento',)
        labels = {  'descsmarcamento': _('Descrizione'),
                 }

class StrutturaForm(forms.ModelForm):
    class Meta:
        model = Struttura
        fields = ('descstruttura',)
        labels = {  'descstruttura': _('Descrizione'),
                 }

class GiudizioForm(forms.ModelForm):
    class Meta:
        model = Giudizio
        fields = ('descgiudizio',)
        labels = {  'descgiudizio': _('Descrizione'),
                 }

class ItemForm(forms.ModelForm):
    piede = forms.ModelChoiceField(queryset=Piede.objects.all())

    class Meta:
        model = Giocatore
        fields = (  'cognome',
                    'nome',
                    'datanascita',
                    'luogonascita',
                    'ruolo',
                    'foto',
                    'telefonogenitore',
                    'telefonogiocatore',
                    'altezza',
                    'piede',
                    'sistemaideale',
                    'societaappertenenza',
                    'scadenzacontratto',
                    'agente',
                    'ingaggio',
                    )

class GaraForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    class Meta:
        model = Gara
        fields = (  'tipo',
                    'categoria',
                    'squadrain',
                    'moduloin',
                    'squadraout',
                    'moduloout',
                    'risultato',
                    'dataincontro',
                    'cognomein1', 'nomein1', 'cognomein2', 'nomein2', 'cognomein3', 'nomein3',
                    'cognomein4', 'nomein4', 'cognomein5', 'nomein5', 'cognomein6', 'nomein6',
                    'cognomein7', 'nomein7', 'cognomein8', 'nomein8', 'cognomein9', 'nomein9',
                    'cognomein10', 'nomein10', 'cognomein11', 'nomein11', 'cognomein12', 'nomein12',
                    'cognomein13', 'nomein13', 'cognomein14', 'nomein14', 'cognomein15', 'nomein15',
                    'cognomein16', 'nomein16',
                    'cognomein17', 'nomein17', 'cognomein18', 'nomein18', 'cognomein19', 'nomein19',
                    'cognomein20', 'nomein20', 'cognomein21', 'nomein21', 'cognomein22', 'nomein22',
                    'cognomein23', 'nomein23', 'cognomein24', 'nomein24', 'cognomein25', 'nomein25',
                    'cognomeout1', 'nomeout1', 'cognomeout2', 'nomeout2', 'cognomeout3', 'nomeout3',
                    'cognomeout4', 'nomeout4', 'cognomeout5', 'nomeout5', 'cognomeout6', 'nomeout6',
                    'cognomeout7', 'nomeout7', 'cognomeout8', 'nomeout8', 'cognomeout9', 'nomeout9',
                    'cognomeout10', 'nomeout10', 'cognomeout11', 'nomeout11', 'cognomeout12', 'nomeout12',
                    'cognomeout13', 'nomeout13', 'cognomeout14', 'nomeout14', 'cognomeout15', 'nomeout15',
                    'cognomeout16', 'nomeout16',
                    'cognomeout17', 'nomeout17', 'cognomeout18', 'nomeout18', 'cognomeout19', 'nomeout19',
                    'cognomeout20', 'nomeout20', 'cognomeout21', 'nomeout21', 'cognomeout22', 'nomeout22',
                    'cognomeout23', 'nomeout23', 'cognomeout24', 'nomeout24', 'cognomeout25', 'nomeout25'
                )

class GiocatoregaraForm(forms.ModelForm):
    struttura = forms.ModelChoiceField(queryset=Struttura.objects.all())
    fisicita = forms.ModelChoiceField(queryset=Fisicita.objects.all())
    calciare = forms.ModelChoiceField(queryset=Calciare.objects.all())
    conduzione = forms.ModelChoiceField(queryset=Conduzione.objects.all())
    controllo = forms.ModelChoiceField(queryset=Controllo.objects.all())
    recuperapalla = forms.ModelChoiceField(queryset=Recuperapalla.objects.all())
    smarcamento = forms.ModelChoiceField(queryset=Smarcamento.objects.all())
    marcatura = forms.ModelChoiceField(queryset=Marcatura.objects.all())
    giocoditesta = forms.ModelChoiceField(queryset=Giocoditesta.objects.all())

    class Meta:
        model = Giocatoregara
        fields = ('struttura',
                  'fisicita',
                  'calciare',
                  'conduzione',
                  'controllo',
                  'recuperapalla',
                  'smarcamento',
                  'marcatura',
                  'giocoditesta',
                  'forza',
                  'resistenza',
                  'velocita',
                  'rapidita',
                  'agilita',
                  'coordinazione',
                  'personalita',
                  'concentrazione',
                  'temperamento',
                  'aggressivita',
                  'autocontrollo',
                  'disponibilita',
                  'assomiglia',
                  'giudizio'
                  )

