from django.db import models

from django.db.models import F, Min, FloatField, Count


class Evento_Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'evento_tipo'
        ordering = ["descricao", ]
        verbose_name_plural = 'Tipos de Eventos'


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    fk_evento_tipo_id = models.ForeignKey(Evento_Tipo, db_column = 'fk_evento_tipo_id', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50)
    dt_evento = models.DateField()
    dt_cad = models.DateField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    # valor_ajustado = models.DecimalField(max_digits=7, decimal_places=2, null=True,  blank=True)
    # valor_final = models.DecimalField(max_digits=7, decimal_places=2, null=True,  blank=True)
    parcelas = models.IntegerField(default=1)
    dt_alt = models.DateField(null=True,  blank=True)
    observacao = models.CharField(max_length=2000, null=True, blank=True)
    # :TODO - more pediu pra importar contrato

    def __str__(self):
        #TODO: retirar parcelas
        return self.descricao + "Valor:" + str(self.valor) + " - Parcelas:" + str(self.parcelas)

    class Meta:
        db_table = 'evento'
        ordering = ["dt_evento", "descricao", ]
        verbose_name_plural = 'Eventos'

    # def getQtLanctos(self):
        # w_count = F.sum(Lancto.objects.get(pk=self.id))
        # w_count = Lancto.objects.filter(lancto__fk_evento_pessoa=F('id'))
        # w_count = Lancto.objects.F('fk_pessoa_pessoa_tipo_id')
        # print("---(EventoPessoaAdmin) - achou Lanctos para Id:"+str(self.id))
        # print("class Evento - getQtLanctos "+str(self.id))

        # w_ret = Evento.objects.annotate(Count('id'))
        # w_ret = Evento.objects.annotate(Count('fk_evento_tipo'))
        # print("class Evento - getQtLanctos => w_ret:" + str(w_ret))

        # w_count = 0
        # for u in w_ret:
        #     # print("...aqui => " + str(u.id__count))
        #     w_count = w_count + u.Evento_Tipo__id

        # qs = Evento.objects.all(). \
        #     annotate(menor=Min('product__quotation__price'), total=pega_total). \

        # w_count = 0
        # w_count = Evento.objects.all().aggregate(campo_aux=Count(F('fk_evento_tipo__id')))['campo_aux']
        # for reg in w_lista:
        #     print(reg.id) #vai imprimir o __str__
        #     w_count = w_count + 1

        # return w_count

    # recuperar qtas pessoas relacionadas no evento
    def getQtEventoPessoa(self):
        # w_count = F.sum(Lancto.objects.get(pk=self.id))
        # w_count = Lancto.objects.filter(lancto__fk_evento_pessoa=F('id'))
        # w_count = Lancto.objects.F('fk_pessoa_pessoa_tipo_id')
        # print("---(EventoPessoaAdmin) - achou Lanctos para Id:"+str(self.id))
        # print("class Evento - getQtLanctos "+str(self.id))

        # w_ret = Evento.objects.annotate(Count('id'))
        # w_ret = Evento.objects.annotate(Count('fk_evento_tipo'))
        # print("class Evento - getQtLanctos => w_ret:" + str(w_ret))

        # w_count = 0
        # for u in w_ret:
        #     # print("...aqui => " + str(u.id__count))
        #     w_count = w_count + u.Evento_Tipo__id

        # qs = Evento.objects.all(). \
        #     annotate(menor=Min('product__quotation__price'), total=pega_total). \

        # w_lista = Evento.objects.raw('select id, descricao from App_Financeiro_lancto where fk_evento_pessoa_id=%s', (self.id) )
        w_count = 0
        # w_count = EventoPessoa.objects.filter().aggregate(campo_aux=Count(F('fk_evento_tipo__id')))['campo_aux']

        # w_lista = Evento.objects.raw('select id, descricao from App_Financeiro_lancto where fk_evento_pessoa_id=%s', (self.id) )
        # w_count = EventoPessoa.objects.all().aggregate(campo_aux=Count(F('fk_evento_tipo__id')))['campo_aux']
        # print("---getQtPessoa---str(self.id):" + str(self.id))

        p_param_id = self.id
        w_lista = Evento.objects.raw('select id from evento_pessoa where fk_evento_id=%s', [p_param_id])
        print("--getQtPessoa---w_lista:" + str(w_lista))
        for reg in w_lista:
             # print(reg) #vai imprimir o __str__
             w_count = w_count + 1

        for reg in w_lista:
            print(reg.id) #vai imprimir o __str__
            w_count = w_count + 1

        return w_count

    # recuperar Valor Total dos Lanctos
    def getLanctoPagar(self):
        w_count = 0
        w_count_pago = 0  # qt parcelas quitadas
        w_valor = 0
        w_valor_pago = 0  # valor parcelas quitadas
        p_param_id = self.id
        w_lista = Evento.objects.raw('select t.id, t.valor, t.dt_pgto '+
                                     'from evento_pessoa evp '+
                                     '   , titulo t '+
                                     'where t.fk_evento_pessoa_id = evp.id and evp.fk_evento_id =%s'+
                                     '  and t.cd_tipo = "P" ',
                                     [p_param_id])

        for reg in w_lista:
             w_count = w_count + 1
             w_valor = w_valor + reg.valor
             if reg.dt_pgto:
                print("Pago => " + str(reg.dt_pgto))
                w_count_pago = w_count_pago + 1
                w_valor_pago = w_valor_pago + reg.valor

        return 'Pago: Parc.:(' + str(w_count_pago) + "/" + str(w_count) + " Valor:(" + str(w_valor_pago) + "/" + str(w_valor) + ")"


    # recuperar Valor Total dos Lanctos
    def getLanctoReceber(self):
        w_count = 0
        w_count_pago = 0  # qt parcelas quitadas
        w_valor = 0
        w_valor_pago = 0  # valor parcelas quitadas
        p_param_id = self.id
        w_lista = Evento.objects.raw('select t.id, t.valor, t.dt_pgto '+
                                     'from Evento_Pessoa evp '+
                                     '   , titulo t '+
                                     'where t.fk_evento_pessoa_id = evp.id and evp.fk_evento_id =%s'+
                                     '  and t.cd_tipo = "R" ',
                                     [p_param_id])
        for reg in w_lista:
             w_count = w_count + 1
             w_valor = w_valor + reg.valor
             if reg.dt_pgto:
                print("Pago => " + str(reg.dt_pgto))
                w_count_pago = w_count_pago + 1
                w_valor_pago = w_valor_pago + reg.valor

        return 'Pago: Parc.:(' + str(w_count_pago) + "/" + str(w_count) + " Valor:(" + str(w_valor_pago) + "/" + str(w_valor) + ")"


from App_Pessoa.models import Pessoa_Pessoa_Tipo


class EventoPessoa(models.Model):
    id = models.AutoField(primary_key=True)
    fk_evento_id = models.ForeignKey(Evento, db_column = 'fk_evento_id',on_delete=models.PROTECT)
    fk_pessoa_pessoa_tipo_id = models.ForeignKey(Pessoa_Pessoa_Tipo, db_column = 'fk_pessoa_pessoa_tipo_id', on_delete=models.PROTECT)

    def __str__(self):
        # print("----self.fk_evento_id:" + str(self.fk_evento_id))
        # print("----self.fk_evento_id:" + self.fk_evento_id)
        # evento = Evento.objects.get(pk = self.fk_evento_id)
        # print("teste: " + evento.descricao)
        return "( Evento:" + str(self.fk_evento_id) + " - Pessoa:" + str(self.fk_pessoa_pessoa_tipo_id)
        # return #evento.descricao

    class Meta:
        db_table = 'evento_pessoa'
        unique_together = (('fk_evento_id', 'fk_pessoa_pessoa_tipo_id', ),)

    # recuperar Valor Total dos Lanctos
    def getLancto(self):
        w_count = 0
        w_valor = 0
        p_param_id = self.id

        w_lista = Evento.objects.raw('select t.id, t.valor as valor '+
                                     'from titulo t '+
                                     'where t.fk_evento_pessoa_id =%s', [p_param_id])

        for reg in w_lista:
             w_count = w_count + 1
             w_valor = w_valor + reg.valor

        return 'QT:' + str(w_count) + " Valor:" + str(w_valor)