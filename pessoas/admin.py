from django.contrib import admin
from .models import Pessoa


class ListandoPessoas(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_display_links = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_per_page = 4


admin.site.register(Pessoa, ListandoPessoas)
