from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=100)


    class Meta:
        db_table = 'evento'
    
    def __str__(self) :
        return self.titulo

    def __str__(self) :
        return self.local

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%MHrs' )


class Endereco(models.Model):
    local = models.CharField(max_length=200)


    def __str__(self) :
        return self.local