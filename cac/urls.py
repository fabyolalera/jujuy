from django.urls import path, re_path

from . import views

urlpatterns = [
    path('',views.index,name='inicio'),
    path('hola_mundo',views.hola_mundo),
    path('saludar/<str:nombre>',views.saludar,name="saludar"),
    path('cursos/detalle/<slug:nombre_curso>',views.cursos_detalle, name="curso_detalle"),
    re_path(r'^cursos/(?P<nombre>\w+)/$',views.cursos,name="cursos")
]