from django.db import models

from App_Evento.models import EventoPessoa
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date

from datetime import datetime

from django.db.models import Count, F


CHOICES_CD_TIPO = (
    ('P', 'Pagar'),
    ('R', 'Receber'),
)

CHOICES_SIM_NAO = (
    ('S', 'Sim'),
    ('N', 'Não'),
)


class Conta(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30)
    dt_cad = models.DateField()
    vl_atual = models.IntegerField()
    cd_status = models.BooleanField(default=True)

    def __str__(self):
      return self.descricao

    class Meta:
        db_table = 'conta'
        ordering = ["descricao"]
        verbose_name_plural = 'Contas'


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30)
    cd_tipo = models.CharField(max_length=1, choices=CHOICES_CD_TIPO)

    def __str__(self):
      return self.descricao

    class Meta:
        db_table = 'grupo'
        ordering = ["descricao"]
        verbose_name_plural = 'Grupos'

    def save(self, force_insert=False, force_update=False):
        if self.descricao == "TESTE":
            return "Yoko não deve nunca ter seu próprio blog"
        else:
            super(Grupo, self).save(force_insert, force_update)  # Chama o método save() "real".


class TipoPagto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30)

    def __str__(self):
      return self.descricao

    class Meta:
        db_table = 'tipo_pagamento'
        ordering = ["descricao"]
        verbose_name_plural = 'Tipos de Pagamentos'


class Orcamento(models.Model):
    id = models.AutoField(primary_key=True)
    fk_grupo_id = models.ForeignKey(Grupo, db_column = 'fk_grupo_id', on_delete=models.PROTECT)
    ano = models.IntegerField()
    mes = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    #TODO: fazer gerar para todos quando for o primeiro mes

    class Meta:
        db_table = 'orcamento'
        verbose_name_plural = 'Orçamentos'
        unique_together = (('fk_grupo_id', 'ano', 'mes'),)

    def __str__(self):
      return 'Teste'


class Conta_Grupo_Tipo_Pagto(models.Model):
    id = models.AutoField(primary_key=True)
    fk_conta_id = models.ForeignKey(Conta, db_column = 'fk_conta_id', on_delete=models.PROTECT)
    fk_grupo_id = models.ForeignKey(Grupo, db_column = 'fk_grupo_id', on_delete=models.PROTECT)
    fk_tipo_pagto_id = models.ForeignKey(TipoPagto, db_column = 'fk_tipo_pagto_id', on_delete=models.PROTECT)
    cd_tipo = models.CharField(max_length=1, choices=CHOICES_CD_TIPO)
    cd_contabil = models.CharField(max_length=1, choices=CHOICES_SIM_NAO)
    obs = models.TextField(max_length=4000, null=True, blank=True)

    class Meta:
        db_table = 'conta_grupo_tipo_pagto'
        verbose_name_plural = 'Parametrização de Conta/Grupo/Tipo Pagto'
        unique_together = (('fk_conta_id', 'fk_grupo_id', 'fk_tipo_pagto_id'),)


class Lancto(models.Model):
    id = models.AutoField(primary_key=True)
    fk_conta_id = models.ForeignKey(Conta, db_column = 'fk_conta_id', on_delete=models.PROTECT)
    fk_grupo_id = models.ForeignKey(Grupo, db_column = 'fk_grupo_id', on_delete=models.PROTECT)
    fk_tipo_pagto_id = models.ForeignKey(TipoPagto, db_column = 'fk_tipo_pagto_id', on_delete=models.PROTECT)
    fk_evento_pessoa_id = models.ForeignKey(EventoPessoa, db_column = 'fk_evento_pessoa_id', on_delete=models.PROTECT, null=True, blank=True)
    descricao = models.CharField(max_length=50)
    dt_cad    = models.DateField()
    dt_vencto = models.DateField()
    dt_pgto   = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    cd_tipo = models.CharField(max_length=1, choices=CHOICES_CD_TIPO)
    parcela = models.IntegerField()
    parcela_total = models.IntegerField()
    dt_alt = models.DateField(null=True, blank=True)
    observacao = models.CharField(max_length=2000, null=True, blank=True)

    #list_display = ['descricao', 'valor']

    def __str__(self):
      return "(" + str(self.id) + ") " + self.descricao

    # @property
    # def get_total(self):
    #     if self.fk_conta:
    #         w_tot = 0
    #         for reg in self.fk_conta.All():
    #             w_tot += 1
    #
    #         return w_tot
    #         # return self.fk_evento_pessoa
    #     else:
    #         return 'Não'

    class Meta:
        db_table = 'titulo'
        ordering = ["dt_vencto", "dt_cad"]
        verbose_name_plural = 'títulos'

def save(self, force_insert=False, force_update=False):
    print("SAVE executando save da transacao...")
    self.dt_alt = datetime.now()
    super(Lancto, self).save(force_insert, force_update)  # Call the "real" save() method.

    if self.dt_pgto is not None:
        print("PAGO")
        return "PAGO"
    else:
        print("NÃO PAGO")
        return "NÃO PAGO"


    # def inserirLanctoManual(self):

    # def getQtLanctos(self):
    #     w_count = 0
    #
    #     aqui
    #
    #     # w_count = Lancto.objects.all().aggregate(countLanctoByEventoPessoa=Count(F('fk_evento_tipo__id')))['countLanctoByEventoPessoa']
    #     print('---lancto:' + str(self.id) + " self.fk_evento_pessoa:" + str(self.fk_evento_pessoa))
    #     # w_count = Lancto.objects.filter(fk_evento_pessoa=str('self.fk_evento_pessoa__id')).aggregate(countLanctoByEventoPessoa=Count(F('fk_evento_pessoa')))['countLanctoByEventoPessoa']
    #               # |filter(fk_evento_pessoa=self.fk_evento_pessoa)
    #
    #     # for reg in w_lista:
    #     #     print(reg.id) #vai imprimir o __str__
    #     #     w_count = w_count + 1
    #
    #     return w_count

@receiver(post_save, sender=Lancto, dispatch_uid="update_stock_count")
def update_stock(sender, instance, created, **kwargs):
    print('POST_SAVE DO @RECEIVER...')
    print('instance.parcela:' + str(instance.parcela)+'/'+str(instance.parcela_total))
    print('PK:'+str(instance.pk))

    if created:
        print('created')
        if instance.parcela_total > 1 and instance.parcela == 1:
            print('---lançar '+str(instance.parcela_total))

            w_new_id = instance.id
            w_new_parcela = instance.parcela
            w_new_dt_vencto = instance.dt_vencto

            while w_new_parcela != instance.parcela_total:
                # novo objeto copiado da instance passada
                w_new_instance = instance
                # TODO: refazer essa logica do +1
                w_new_id = w_new_id + 1
                w_new_instance.id = w_new_id
                # TODO: refazer essa logica do +30
                w_new_dt_vencto = date.fromordinal(w_new_dt_vencto.toordinal()+30)
                w_new_instance.dt_vencto = w_new_dt_vencto

                w_new_parcela = w_new_parcela + 1
                w_new_instance.parcela = w_new_parcela

                print('novo valor do new:' + str(w_new_instance.id))
                print('novo parcela do new:' + str(w_new_instance.parcela))
                instance.save();

    else:
        print('NOT created')



    # instance.product.save()

    # def post_save(self, force_insert=False, force_update=False):
    #     print("POST_SAVE executando save da transacao...")
    #     super(Lancto, self).post_save(force_insert, force_update)  # Call the "real" save() method.
    #
    #     if self.dt_pgto is not None:
    #         print("PAGO")
    #         return "PAGO"
    #     else:
    #         print("NÃO PAGO")
    #         return "NÃO PAGO"
    #
    #
    # def post_insert(self, force_insert=False, force_update=False):
    #     print("POST_INSERT executando save da transacao...")
    #     super(Lancto, self).post_insert(force_insert, force_update)  # Call the "real" save() method.
    #
    #     if self.dt_pgto is not None:
    #         print("PAGO")
    #         return "PAGO"
    #     else:
    #         print("NÃO PAGO")
    #         return "NÃO PAGO"


class LanctoExtrato(models.Model):
    id = models.AutoField(primary_key=True)
    fk_titulo_id = models.ForeignKey(Lancto, db_column = 'fk_titulo_id', on_delete=models.PROTECT)
    dt_cad = models.DateField()
    valor_saldo_anterior = models.DecimalField(max_digits=7, decimal_places=2)
    valor_saldo_atualizado = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'titulo_extrato'
        verbose_name_plural = 'Extrato da Conta'

    #TODO: ver como colocar read only
    #TODO: criar opção de estorno ou deixar apenas para consultar a TRANSACAO e estornar por lá