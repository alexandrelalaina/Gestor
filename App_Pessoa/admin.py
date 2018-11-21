from django.contrib import admin

from .models import Pessoa_Tipo, Pessoa, Contato_Tipo, Endereco_Tipo, Endereco, Contato, Pessoa_Pessoa_Tipo


########## P e s s o a - A d m i n ###############################
class PessoaContatoInline(admin.TabularInline):
    model = Contato
    extra = 1 #qtos itens serao mostrados


class PessoaEnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1 #qtos itens serao mostrados


class PessoaPessoaTipoInline(admin.TabularInline):
    model = Pessoa_Pessoa_Tipo
    extra = 1 #qtos itens serao mostrados


class PessoaAdmin(admin.ModelAdmin):
    inlines = [PessoaContatoInline, PessoaEnderecoInline, PessoaPessoaTipoInline]
    list_display = ['id', 'nome', ]
    search_fields = ['id', 'nome', ]

class Evento_TipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', ]
    search_fields = ['id', 'descricao', ]


class PessoaTipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', ]
    search_fields = ['id', 'descricao', ]

admin.site.register(Pessoa_Tipo, PessoaTipoAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato_Tipo)
admin.site.register(Endereco_Tipo)
admin.site.register(Endereco)
admin.site.register(Contato)
admin.site.register(Pessoa_Pessoa_Tipo)
