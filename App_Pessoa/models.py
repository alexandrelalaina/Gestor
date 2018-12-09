from django.db import models

CHOICES_CD_SIT = (
    (1, 'Ativo'),
    (0, 'Inativado'),
)


class Pessoa_Tipo(models.Model):
   id = models.AutoField(primary_key=True)
   descricao = models.CharField(max_length=30)

   def __str__(self):
     return self.descricao

   class Meta:
     db_table = 'pessoa_tipo'
     ordering = ["descricao",]
     verbose_name_plural = 'Tipos de Pessoas'


class Contato_Tipo(models.Model):
   id = models.AutoField(primary_key=True)
   descricao = models.CharField(max_length=30)

   def __str__(self):
     return self.descricao

   class Meta:
     db_table = 'contato_tipo'
     ordering = ["descricao",]
     verbose_name_plural = 'Tipos de Contatos'


class Endereco_Tipo(models.Model):
   id = models.AutoField(primary_key=True)
   descricao = models.CharField(max_length=30)

   def __str__(self):
     return self.descricao

   class Meta:
     db_table = 'endereco_tipo'
     ordering = ["descricao",]
     verbose_name_plural = 'Tipos de Endereços'


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cd_sit = models.IntegerField(default=1, choices=CHOICES_CD_SIT)
    dt_cad = models.DateField()#default=DateTime.now)
    apelido = models.CharField(max_length=50, null=True, blank=True)
    dt_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    rg = models.CharField(max_length=10, null=True, blank=True)
    obs = models.TextField(max_length=4000, null=True, blank=True)

    def __str__(self):
      return self.nome

    class Meta:
        db_table = 'pessoa'
        ordering = ["nome", "dt_cad"]
        verbose_name_plural = 'Pessoas'


class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    fk_contato_tipo_id = models.ForeignKey(Contato_Tipo, db_column = 'fk_contato_tipo_id', on_delete=models.PROTECT)
    fk_pessoa_id = models.ForeignKey(Pessoa, db_column = 'fk_pessoa_id', on_delete=models.PROTECT)
    vl_alfa = models.CharField(max_length=30)

    def __str__(self):
      return self.vl_alfa

    class Meta:
        db_table = 'contato'
        ordering = ["vl_alfa", ]
        verbose_name_plural = 'Contatos'


class Pessoa_Pessoa_Tipo(models.Model):

    class Meta:
        db_table = 'pessoa_pessoa_tipo'
        unique_together = (('fk_pessoa_id', 'fk_pessoa_tipo_id'),)
        verbose_name_plural = 'Pessoa Tipos'

    id = models.AutoField(primary_key=True)
    fk_pessoa_id = models.ForeignKey(Pessoa, db_column = 'fk_pessoa_id', on_delete=models.PROTECT)
    fk_pessoa_tipo_id = models.ForeignKey(Pessoa_Tipo, db_column = 'fk_pessoa_tipo_id',  on_delete=models.PROTECT)

    def __str__(self):
      #TODO: Ajustar aqui
      return "(" + str(self.id) + ") " +  str(self.fk_pessoa_id) + " (" + str(self.fk_pessoa_tipo_id) + ')'
      # return str(self.id)
      # return str(self.fk_pessoa_id)


from App_Evento.models import Evento

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    fk_endereco_tipo_id = models.ForeignKey(Endereco_Tipo, db_column = 'fk_endereco_tipo_id', on_delete=models.PROTECT)
    #todo: fazer uma validacao para ser um ou outro
    fk_pessoa_id = models.ForeignKey(Pessoa, db_column = 'fk_pessoa_id',  on_delete=models.PROTECT, blank=True, null=True)
    fk_evento_id = models.ForeignKey(Evento, db_column = 'fk_evento_id',  on_delete=models.PROTECT, blank=True, null=True)
    cep = models.IntegerField(null=True, blank=True)
    pais = models.CharField(max_length=20, null=True, blank=True)
    uf = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    endereco = models.CharField(max_length=30)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=20, null = True, blank = True)
    referencia = models.CharField(max_length=50, null = True, blank = True)
    obs = models.TextField(max_length=4000, null=True, blank=True)

    def __str__(self):
      return self.endereco

    class Meta:
      db_table = 'endereco'
      verbose_name_plural = 'Endereços'


