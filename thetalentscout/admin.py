# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Piede, Giocatore

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
from .models import Giudizio
from .models import Fotogiocatoregara

admin.site.register(Giocatore)
admin.site.register(Gara)
admin.site.register(Giocatoregara)
admin.site.register(Struttura)
admin.site.register(Piede)
admin.site.register(Conduzione)
admin.site.register(Recuperapalla)
admin.site.register(Marcatura)
admin.site.register(Categoria)
admin.site.register(Fisicita)
admin.site.register(Calciare)
admin.site.register(Controllo)
admin.site.register(Smarcamento)
admin.site.register(Giocoditesta)
admin.site.register(Giudizio)
admin.site.register(Fotogiocatoregara)
