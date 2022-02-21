from django.db import models

# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=256, null=False)
    logradouro = models.CharField(max_length=256, null=False)
    complemento = models.CharField(max_length=256, null=True, blank=True)
    bairro = models.CharField(max_length=256, null=False, blank=True)
    localidade = models.CharField(max_length=256, null=False, blank=True)
    uf = models.CharField(max_length=256, null=False, blank=True)
    ibge = models.CharField(max_length=256, null=True, blank=True)
    gia = models.CharField(max_length=256, null=True, blank=True)
    ddd = models.CharField(max_length=256, null=True, blank=True)
    siafi = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.cep
