from django.db import models
from users.models import User

# Create your models here.

class Pago(models.Model):
    servicio_v1 = models.CharField(max_length=100,null=True)
    monto = models.FloatField(default=0.0)
    fecha_pago = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')

    def __str__(self):
        return self.servicio_v1
