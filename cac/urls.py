from django.urls import path, re_path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='inicio'),
    path('quienessomos/',views.quienes_somos,name='quienes_somos'),
    path('proyectos_puna/',views.ver_proyectos_puna, name='proyectos_puna'),
    path('cursos_puna/',views.ver_cursos_puna, name='cursos_puna'),
    path('api_proyectos_puna/',views.api_proyectos_puna,name="api_proyectos_puna"),
    path('cursos_quebrada/',views.ver_cursos_quebrada, name='cursos_quebrada'),
   
    path('cursos_yunga/',views.ver_cursos_yunga, name='cursos_yunga'),
    path('cursos_valle/',views.ver_cursos_valle, name='cursos_valle'),
    path('contacto/',views.contacto, name='contacto'),
    path('administracion', views.index_administracion,name='inicio_administracion'),
   
    path('administracion/categorias', views.categorias_index,name='categorias_index'),
    path('administracion/categorias/nuevo', views.categorias_nuevo,name='categorias_nuevo'),
    path('administracion/categorias/eliminar/<int:id_categoria>', views.categorias_eliminar,name='categorias_eliminar'),
    path('administracion/cursos', views.cursos_index,name='cursos_index'),
    path('administracion/cursos/nuevo/', views.cursos_nuevo,name='cursos_nuevo'),
    path('administracion/cursos/editar/<int:id_curso>', views.cursos_editar,name='cursos_editar'),
    path('administracion/cursos/eliminar/<int:id_curso>', views.cursos_eliminar,name='cursos_eliminar'),

    path('administracion/estudiantes', views.estudiantes_index,name='estudiantes_index'),
    path('administracion/estudiantes/nuevo/', views.estudiantes_nuevo,name='estudiantes_nuevo'),
    path('administracion/estudiantes/editar/<int:id_estudiante>', views.estudiantes_editar,name='estudiantes_editar'),
    path('administracion/estudiantes/eliminar/<int:id_estudiante>', views.estudiantes_eliminar,name='estudiantes_eliminar'),

    path('administracion/proyectos', views.proyectos_index,name='proyectos_index'),
    path('administracion/proyectos/nuevo/', views.proyectos_nuevo,name='proyectos_nuevo'),
    path('administracion/proyectos/editar/<int:id_proyecto>', views.proyectos_editar,name='proyectos_editar'),
    path('administracion/proyectos/eliminar/<int:id_proyecto>', views.proyectos_eliminar,name='proyectos_eliminar'),

    
    
    path('hola_mundo',views.hola_mundo),
    path('saludar/<str:nombre>',views.saludar,name="saludar"),
    #path('cursos/detalle/<slug:nombre_curso>',views.cursos_detalle, name="curso_detalle"),
    #re_path(r'^cursos/(?P<nombre>\w+)/$',views.cursos,name="cursos")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 