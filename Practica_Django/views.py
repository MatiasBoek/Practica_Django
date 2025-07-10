from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f'<h1> {fecha.strftime('%H:%M:%S')}: Hola {nombre} {apellido}</h1>')

def saludo_template(request, nombre, apellido):
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido, 
    }
       
    #with open(r'C:\documentos\1. CODERHOUSE\Python\Practica_DJANGO\Practica_Django\templates\saludo_template.html'):
    
    #archivo_abierto = open(r'C:\documentos\1. CODERHOUSE\Python\Practica_DJANGO\Practica_Django\templates\saludo_template.html') RUTA ABSOLUTA
    
    archivo_abierto = open(r'Practica_DJANGO\Practica_Django\templates\saludo_template.html') #RUTA RELATIVA
    template = Template (archivo_abierto.read())
    archivo_abierto.close()
        
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto) #Crea un formato HTML legible para que se lo pueda pasar al navegador. 
       
    return HttpResponse(template_renderizado)

def saludo_con_cargador(request, nombre, apellido):
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido, 
    }
       
    archivo_abierto = open(r'Practica_DJANGO\Practica_Django\templates\saludo_template.html') #RUTA RELATIVA
    template = Template (archivo_abierto.read())
    archivo_abierto.close()
    
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto) #Crea un formato HTML legible para que se lo pueda pasar al navegador. 
       
    return HttpResponse(template_renderizado)


