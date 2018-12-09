from django.db import models

from django.urls import reverse

from App_Evento.models import Evento, Evento_Tipo
from App_Financeiro.models import Conta, Grupo, Lancto
from App_Pessoa.models import Pessoa


CHOICES_CD_TIPO_UTILIZACAO = (
    ('T', 'Tabela'),
    ('A', 'Assunto'),
)

CHOICES_CD_INFO_OBRIGATORIA = (
    ('N/A', 'Nenhuma'),
    ('N', 'Valor numérico'),
    ('A', 'Valor alfa'),
    ('D', 'Data'),
)


class CaractTipo(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    cd_tipo_utilizacao = models.CharField(max_length=30, choices=CHOICES_CD_TIPO_UTILIZACAO, help_text="Como será utilizado. Ex: tabela, por assunto e etc.")
    # :TODO ver uma forma de trazer as tabelas e tbm liberar registro livre
    cd_utilizado_em = models.CharField(max_length=30, help_text="Onde está sendo utilizado. Ex: tabela evento, processo pagamento e etc.")
    cd_info_obrigatoria = models.CharField(max_length=20, choices=CHOICES_CD_INFO_OBRIGATORIA, help_text="Informação que será exigida. Ex: valor, alfanumérico ou data.")
    # TODO: --informacao que será exigida no preenchimento da caract_relacionada (validar na programacao)
    dt_cad = models.DateTimeField(auto_now_add=True)
    obs = models.TextField(max_length=4000, null=True, blank=True)

    class Meta:
      db_table = 'caract_tipo'
      ordering = ["descricao",]
      verbose_name_plural = 'Tipos de Características'

    def __str__(self):
        # return 'teste'  # self.rv_domain
        return str(self.id) + ' (' + self.descricao + ' - ' + self.cd_tipo_utilizacao + '/' + self.cd_utilizado_em + ')'


class CaractRel(models.Model):
    id = models.AutoField(primary_key=True)
    fk_caract_tipo_id = models.ForeignKey(CaractTipo, db_column='fk_caract_tipo_id', on_delete=models.PROTECT)
    fk_evento_id = models.ForeignKey(Evento, db_column='fk_evento_id', on_delete=models.PROTECT, null=True, blank=True)
    fk_evento_tipo_id = models.ForeignKey(Evento_Tipo, db_column='fk_evento_tipo_id', on_delete=models.PROTECT, null=True, blank=True)
    fk_conta_id = models.ForeignKey(Conta, db_column='fk_conta_id', on_delete=models.PROTECT, null=True, blank=True)
    fk_grupo_id = models.ForeignKey(Grupo, db_column='fk_grupo_id', on_delete=models.PROTECT, null=True, blank=True)
    fk_titulo_id = models.ForeignKey(Lancto, db_column='fk_titulo_id', on_delete=models.PROTECT, null=True, blank=True)
    fk_pessoa_id = models.ForeignKey(Pessoa, db_column='fk_pessoa_id', on_delete=models.PROTECT, null=True, blank=True)
    dt_cad = models.DateTimeField(auto_now_add=True)
    # TODO: trabalhar com o us_cad
    us_cad = models.CharField(max_length=30, default="ROOT")
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) #123.456,78
    valor_alfa = models.CharField(max_length=30, null=True, blank=True)
    data = models.DateTimeField(null=True, blank=True)
    obs = models.TextField(max_length=4000, null=True, blank=True)

    class Meta:
      db_table = 'caract_rel'
      # TODO: alterar ordenacao
      ordering = ["id",]
      verbose_name_plural = 'Características Relacionadas'

    def __str__(self):
        return "caract_rel.id:"+str(self.id) + " Tipo_caract:" + str(self.fk_caract_tipo_id) + " Valor:" + str(self.valor) + " Evento:"+str(self.fk_evento_id) + " Conta:"+str(self.fk_conta_id) + " Grupo:" + str(self.fk_grupo_id) + " Titulo:" + str(self.fk_titulo_id)+ " Pessoa:" + str(self.fk_pessoa_id)

    def get_absolute_url(self):
        return reverse('get_absolute_url')