# from django.http import HttpResponse,HttpResponseRedirect
# from django.template.loader import get_template 
# from django.template import Context
# from datetime import datetime
from django.shortcuts import render_to_response
# from demo.forms import *
from django.template.context import RequestContext

from website.models import * #modelos de la app website


def home(request):
    servicios = servicio.objects.all()

    return render_to_response("base.html",context_instance=RequestContext(request,{'servicios':servicios})) 
    #context_instance=RequestContext(request) sirve para trabajar con archivos estaticos

	
# def index(request):
#     libros = Libro.objects.all()
#     return render_to_response('galeria.html', 
#     						context_instance=RequestContext(request,{'libros': libros}))