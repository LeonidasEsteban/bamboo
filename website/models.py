from django.db import models

# Create your models here.

class servicio(models.Model):
	nombre = models.CharField(blank=True, max_length=100) #input["text"]
	clase = models.CharField(blank=True, max_length=100) #input["text"]
	descripcion = models.TextField("descripcion del servicio")

	def __unicode__(self):
		return self.nombre