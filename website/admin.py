from django.contrib import admin
from website.models import * #importando todos los modelos de la app website

admin.site.register(servicio)#registrando servicio en la bd

#lo minimo para importar los modelos que queremos pasar a bd