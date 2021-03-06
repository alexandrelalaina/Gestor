from django.contrib import admin

from .models import Conta, Grupo, TipoPagto, Lancto, LanctoExtrato, Orcamento, Conta_Grupo_Tipo_Pagto
from .actions import pagar_receber


class OrcamentoInline(admin.TabularInline):
    model = Orcamento
    extra = 1 #qtos itens serao mostrados


class ContaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao']
    search_fields = ['id', 'descricao']


class GrupoAdmin(admin.ModelAdmin):
    inlines = [OrcamentoInline, ]
    list_display = ['id', 'descricao']
    search_fields = ['id', 'descricao']


# def make_published(modeladmin, request, queryset):
#     queryset.update(status='P')
#
# make_published.short_description = "Teste"
#
#
# class transacao(admin.ModelAdmin):
#     actions = [make_published]


class LanctoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'dt_cad', 'dt_vencto', 'dt_pgto', 'valor', 'cd_tipo', 'parcela', 'parcela_total', 'fk_conta_id', 'fk_grupo_id', 'fk_tipo_pagto_id', 'fk_evento_pessoa_id',  'dt_alt', ]
    # fields = [ ('descricao', 'fk_evento_pessoa'),
    #            ('fk_conta', 'fk_grupo', 'fk_tipo_pagto'),
    #            ('dt_cad', 'dt_vencto', 'dt_pgto'),
    #            ('valor', 'cd_tipo', 'parcela', 'parcela_total'),
    #            'observacao'
    # ]

    # fieldsets = ( ('Datas',
    #                  {'classes': ('collapse',),
    #                  'fields':  ('dt_cad', 'dt_vencto', 'dt_pgto'),}),
    #
    #               )

    list_filter = ('fk_conta_id', 'fk_grupo_id', 'fk_tipo_pagto_id', 'dt_cad', 'dt_vencto', 'dt_pgto', )
    search_fields = ['descricao']

    # continuar aqiuo autocomplete

    actions = [pagar_receber]

    #fields = ['descricao']
    #exclude = ['observacao']


admin.site.register(Conta, ContaAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(TipoPagto)
admin.site.register(Lancto, LanctoAdmin)
admin.site.register(LanctoExtrato)
admin.site.register(Orcamento)
admin.site.register(Conta_Grupo_Tipo_Pagto)

actions = ['some_other_action']

#exlcuir a ACTION de delete
#admin.site.disable_action('delete_selected')
