from datetime import datetime
from multiprocessing import context

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from cac.forms import (CategoriaForm, CategoriaFormValidado, ContactoForm,
                       CursoForm, EstudianteMForm, ProyectoForm)
from cac.models import Categoria, Curso, EstudianteM, Proyecto

"""
    Vistas de la parte pública
"""
# Create your views here.
def index(request):
 
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    
    return render(request,'cac/publica/index.html',{'cursos':listado_cursos,})

def contacto(request):
    if(request.method == 'POST'):
            contacto_form = ContactoForm(request.POST)
            if(contacto_form.is_valid()):
    
                pass
                messages.success(request,'Muchas gracias por contactarte, te esteremos respondiendo en breve.')
            #    messages.info(request,'Otro mensajito')
            #deberia validar y realizar alguna accion   
            else:
                messages.warning(request,'Por favor revisa los errores')     
    else:
        contacto_form = ContactoForm()
    return render(request,'cac/publica/contacto.html',
                {'contacto_form':contacto_form})





def quienes_somos(request):
     #return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    template = loader.get_template('cac/quienes_somos.html')
    context = {'titulo':'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(context,request))

def ver_proyectos_puna(request,anio=2022,mes=1):
    proyectos_puna = []
    return render(request,'cac/publica/proyectos_puna.html',{'proyectos':proyectos_puna})

def api_proyectos_puna(request,):
    
    proyectos_puna = [{
        "id":1,
        "titulo": "Cusi Cusi",
        "reseña":"El Valle de la Luna está posicionado en una amplia hoyada labrada fundamentalmente sobre distintos tipos de arcillas",
        
        "image=":  " carnaval.jpg "  ,
            
    },
    {
        "id":2,
        "titulo": "Abra Pampa",
        "reseña":"El pueblo presenta una arquitectura sencilla presente en su iglesia, estación de trenes entre otros.</br> Es sede también del Festival del Huancar y de la Fiesta de la Pachamama. ",
        "image":"Puna2AbraPampa.png"
    },
    {
        "id":3,
        "titulo": "El Moreno",
        "reseña":"El Moreno pueblo de encanto al pie del Cerro Chañi, testigo de caminos ancestrales y apus venerados por pueblos prehispánicos. Ubicado en el departamento Tumbaya",
        "image": "url('imagenes/Puna3ElMoreno.png')"
    },
    {
        "id":4,
        "titulo": "El Huancar",
        "reseña":"Se trata de un médano gigante situado en Abra Pampa. Al pie del cerro existe una laguna",
        "image":"imagenes/Puna4Huancar.png"
      
        
    },
    {
        "id":5,
        "titulo": "Laguna de Pozuelos",
        "reseña":"La Laguna de Pozuelos con sus 15.000 hectáreas de extensión fue declarada como Monumento Natural en el año 1981 por su importancia como hábitat de numerosas especies de aves",
        "image":"imagenes/Puna5Pozuelos.png"
    },
    {
        "id":6,
        "titulo": "Camino del Inca",
        "reseña":"El circuito parte de la localidad de Santa Ana (3350 msnm) y culmina en Valle Colorado (1962 msnm). El plus es nada menos que, evocar el poderoso Imperio Inca.",
        "image":"imagenes/Puna6Montanismo.png"
    },
    {
        "id":7,
        "titulo": "Yavi",
        "reseña":"Visitar Yavi implica conocer la magnífica iglesia consagrada a San Francisco de Asís y la famosa Casa del Marqués, edificios ubicados uno frente al otro.",
        
        "image": "<img src=cac/publica/imagenes/Puna7Yavi.png>",
            
    },
    {
        "id":8,
        "titulo": "Casabindo",
        "reseña":"El pueblo puneño del toreo se encuentra ubicado a 3603 metros sobre el nivel del mar, en el corazón del departamento de Cochinoca",
        "image":"imagenes/Puna8Casabindo.png"
    },]
    response = {'status':'Ok','code':200,'message':'Listado de proyectos','data':proyectos_puna}
    return JsonResponse(response,safe=False)


def ver_cursos_puna(request):
    listado_cursos_puna = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    return render(request,'cac/publica/cursos_puna.html',{'cursos':listado_cursos_puna})

def ver_cursos_quebrada(request):
    listado_cursos_quebrada = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    return render(request,'cac/publica/cursos_quebrada.html',{'cursos_quebrada':listado_cursos_quebrada})

def ver_cursos_valle(request):
    listado_cursos_valle = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    return render(request,'cac/publica/cursos_valle.html',{'cursos':listado_cursos_valle})

def ver_cursos_yunga(request):
    listado_cursos_yunga = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    return render(request,'cac/publica/cursos_yunga.html',{'cursos':listado_cursos_yunga})


"""
    Vistas de la parte administracion
"""
def index_administracion(request):
    variable = 'test variable'
    return render(request,'cac/administracion/index_administracion.html',{'variable':variable})

"""
    CRUD Categorias
"""
def categorias_index(request):
    #queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request,'cac/administracion/categorias/index.html',{'categorias':categorias})

def categorias_nuevo(request):
    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            nueva_categoria = Categoria(nombre=nombre)
            nueva_categoria.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request,'cac/administracion/categorias/nuevo.html',{'formulario':formulario})

def categorias_eliminar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')

"""
    CRUD Cursos
"""

def cursos_index(request):
    cursos = Curso.objects.all()
    return render(request,'cac/administracion/cursos/index.html',{'cursos':cursos})

def cursos_nuevo(request):
    #forma de resumida de instanciar un formulario basado en model con los
    #datos recibidos por POST si la petición es por POST o bien vacio(None)
    #Si la petición es por GET
    formulario = CursoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el curso correctamente')          
        return redirect('cursos_index')
    return render(request,'cac/administracion/cursos/nuevo.html',{'formulario':formulario})

def cursos_editar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    formulario = CursoForm(request.POST or None,request.FILES or None,instance=curso)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado el curso correctamente')          
        return redirect('curso_index')
    return render(request,'cac/administracion/cursos/editar.html',{'formulario':formulario})

def cursos_eliminar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    messages.success(request,'Se ha eliminado el curso correctamente')          
    curso.delete()
    return redirect('cursos_index')

"""
    CRUD Estudiantes
"""

def estudiantes_index(request):
    estudiantes = EstudianteM.objects.all()
    return render(request,'cac/administracion/estudiantes/index.html',{'estudiantes':estudiantes})

def estudiantes_nuevo(request):
    formulario = EstudianteMForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado al estudiante correctamente')          
        return redirect('estudiantes_index')
    return render(request,'cac/administracion/estudiantes/nuevo.html',{'formulario':formulario})

def estudiantes_editar(request,id_estudiante):
    try:
        estudiante = EstudianteM.objects.get(pk=id_estudiante)
    except EstudianteM.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    formulario = EstudianteMForm(request.POST or None,request.FILES or None,instance=estudiante)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado al estudiante correctamente')          
        return redirect('estudiantes_index')
    return render(request,'cac/administracion/estudiantes/editar.html',{'formulario':formulario})

def estudiantes_eliminar(request,id_estudiante):
    try:
        estudiante = Proyecto.objects.get(pk=id_estudiante)
    except Proyecto.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    estudiante.delete()
    messages.success(request,'Se ha eliminado al estudiante correctamente')          
    return redirect('proyectos_index')

"""
    CRUD Proyectos
"""

def proyectos_index(request):
    proyectos = Proyecto.objects.all()
    return render(request,'cac/administracion/proyectos/index.html',{'proyectos':proyectos})

def proyectos_nuevo(request):
    formulario = ProyectoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el proyecto correctamente')          
        return redirect('proyectos_index')
    return render(request,'cac/administracion/proyectos/nuevo.html',{'formulario':formulario})

def proyectos_editar(request,id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
    except Proyecto.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    formulario = ProyectoForm(request.POST or None,request.FILES or None,instance=proyecto)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado el proyecto correctamente')          
        return redirect('proyectos_index')
    return render(request,'cac/administracion/proyectos/editar.html',{'formulario':formulario})

def proyectos_eliminar(request,id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
    except Proyecto.DoesNotExist:
        return render(request,'cac/administracion/404_admin.html')
    messages.success(request,'Se ha eliminado el proyecto correctamente')          
    proyecto.delete()
    return redirect('proyectos_index')

class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'lista_categorias'
    template_name= 'cac/administracion/categorias/index.html'
    queryset= Categoria.objects.filter(baja=False)
    ordering = ['nombre']
class CategoriaView(View):
    form_class = CategoriaForm
    template_name = 'cac/administracion/categorias/nuevo.html'
    def get(self, request,*args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{'formulario':form})
    
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias_index')
        return render(request,self.template_name,{'formulario':form})


def hola_mundo(request):
    return HttpResponse('Hola mundo Django')

def saludar(request,nombre='Pepe'):
    return HttpResponse(f"""
        <h1>Hola Mundo - {nombre}</h1>
        <p>Esto es una prueba</p>
    """)
    
def cursos_detalle(request,nombre_curso):
    return HttpResponse(f"""
        <h1>{nombre_curso}</h1>
    """)


def cursos(request,nombre):
    return HttpResponse(f"""
        <h2>{nombre}</h2>
    """)
    
