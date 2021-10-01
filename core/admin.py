from django.contrib import admin
from core.models import Evento, Endereco
# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao','local')
    list_filter = ('usuario','data_evento','local')

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Evento, EventoAdmin)
admin.site.register(Endereco, EnderecoAdmin)