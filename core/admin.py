from django.contrib import admin
from .models import Endereco

# Register your models here.


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("cep", "logradouro", "complemento", "bairro", "localidade", "uf")
    list_display_links = ("cep", "logradouro")
    search_fields = ("cep", "logradouro", "bairro")
    list_per_page = 20


admin.site.register(Endereco, EnderecoAdmin)
