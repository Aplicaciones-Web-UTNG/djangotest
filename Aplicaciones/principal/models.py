from django.db import models

# Create your models here.

class Persona(models.Model):
    # Modelo de la tabla creada en SQL3
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, unique = True)
    apellido = models.CharField(max_length = 100, unique = True)
    correo = models.EmailField(max_length = 200, unique = True)

    def __str__(self):
        texto = "{1} {2} {3}" 
        return texto.format(self.id, self.nombre, self.apellido, self.correo) 
