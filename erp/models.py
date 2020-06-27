
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Clientes(models.Model):
    clientes_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.clientes_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?' 
    list_filter = ['pub_date']  
    search_fields = ['clientes_text'] 
   


class Informes(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    informes_text = models.CharField(max_length=200)
    Monto_Pesos = models.IntegerField(default=0)
    Persona_o_entidad= models.CharField(max_length = 80)
    Recivido =  models.BooleanField(null=True)
    Enviado = models.BooleanField(null=True)
    Saldo_Total = models.IntegerField(default=0)

   
    def __str__(self):
        return self.informes_text


class Pagos(models.Model):
    clientes_text = models.CharField(max_length=200)
    pagos_text = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=0)
    efectivo = models.IntegerField(default=0)
    tarjeta = models.IntegerField(default=0)
    bancario = models.IntegerField(default=0)
    adelanto = models.IntegerField(default=0)
    sesenta =  models.IntegerField(default=0)
    treinta =  models.IntegerField(default=0)
    diez =  models.IntegerField(default=0)
    def __str__(self):
        return self.pagos_text       


        





