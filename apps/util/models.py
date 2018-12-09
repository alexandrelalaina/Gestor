from django.db import models
from datetime import datetime

class CgRefCodes(models.Model):

    class Meta:
      db_table = 'cg_ref_codes'
      ordering = ["rv_domain", "rv_low_value",]
      verbose_name_plural = 'cg_ref_codes'

    def __str__(self):
        # return 'teste'  # self.rv_domain
        return self.rv_domain + ' (' + self.rv_low_value + ' - ' + self.rv_meaning + ')'

    id = models.AutoField(primary_key=True)
    # TODO: colocar tudo em maiuscula
    rv_domain = models.CharField(max_length=100, help_text="Domínio a ser utilizado. Ex: tabela.coluna")
    rv_low_value = models.CharField(max_length=240, help_text="Valor de relacionamento")
    rv_high_value = models.CharField(max_length=240, help_text="Valor auxiliar de relacionamento")
    rv_meaning = models.CharField(max_length=240)
    rv_abbreviation = models.CharField(max_length=240, null=True, blank=True)
    # dt_cad = models.DateField(default=DateTime.now)))
    dt_cad = models.DateTimeField(auto_now_add=True)
    # dt_cad = models.DateTimeField(default=datetime.now, auto_now_add=True)