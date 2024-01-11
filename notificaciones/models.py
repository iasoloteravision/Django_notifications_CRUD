# notificaciones/models.py
from django.db import models


class Notificacion(models.Model):
    mensaje = models.CharField(max_length=255)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.mensaje
