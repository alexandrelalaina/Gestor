def pagar_receber(modeladmin, request, queryset):
    print('action = pagar_receber')
    queryset.update(observacao="pago")

pagar_receber.short_description = "PagarReceber"