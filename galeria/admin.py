from django.contrib import admin
from galeria.models import Fotografia

# Se não criar essa classe para exbir a lista das fotografias no banco então será utilizada o __str__ do model Fotografia
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicar")
    list_display_links = ("id", "nome", "legenda")
    # tem que ter uma virgula no final porque é esperado uma tupla
    search_fields = ("nome", "legenda", )
    list_filter = ("categoria","publicar",)
    list_editable = ("publicar",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
