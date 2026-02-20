from django.db import models


class LeadContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    local = models.CharField(max_length=150)
    # NUEVO CAMPO:
    redes_sociales = models.CharField(max_length=255, blank=True, null=True) 
    mensaje = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.nombre} - {self.local}"