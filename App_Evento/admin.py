from django.contrib import admin

from .models import Evento_Tipo, Evento, EventoPessoa
from App_Pessoa.models import Endereco
from App_Financeiro.models import Lancto


########## E v e n t o - A d m i n ###############################
class LanctoInline(admin.TabularInline):
    model = Lancto
    extra = 1 #qtos itens serao mostrados

class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1 #qtos itens serao mostrados


class EventoPessoaInline(admin.TabularInline):
    model = EventoPessoa
    extra = 1 #qtos itens serao mostrados
    inlines = [LanctoInline]


class EventoPessoaAdmin(admin.ModelAdmin):
    inlines = [LanctoInline]
    list_display = ['id', 'getLancto', 'fk_evento_id', 'fk_pessoa_pessoa_tipo_id', ]


class EventoAdmin(admin.ModelAdmin):
    inlines = [EnderecoInline, EventoPessoaInline]
    list_display = ['id', 'getQtEventoPessoa', 'getLanctoPagar', 'getLanctoReceber',  'fk_evento_tipo_id', 'descricao', 'dt_evento', 'dt_cad', 'valor', 'parcelas', 'dt_alt', ]
    list_filter = ( 'fk_evento_tipo_id', 'dt_evento', 'dt_cad', 'valor', )
    search_fields = ['id', 'descricao', 'fk_evento_tipo_id__descricao']
    #link_fields = ('id', 'fk_evento_tipo', 'descricao')


class Evento_TipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', ]
    search_fields = ['id', 'descricao', ]


admin.site.register(Evento, EventoAdmin)
admin.site.register(Evento_Tipo, Evento_TipoAdmin)
admin.site.register(EventoPessoa, EventoPessoaAdmin)
