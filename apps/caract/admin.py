from django.contrib import admin
from .models import CaractTipo, CaractRel


class CaractTipoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'descricao']


class CaractRelAdmin(admin.ModelAdmin):
    autocomplete_fields = ['fk_caract_tipo_id', 'fk_evento_id', 'fk_conta_id', 'fk_grupo_id', 'fk_titulo_id', 'fk_pessoa_id']


admin.site.register(CaractTipo, CaractTipoAdmin)
admin.site.register(CaractRel, CaractRelAdmin)
