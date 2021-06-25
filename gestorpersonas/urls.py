from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name="lista_personas"),
    path('detalles/<int:pk>', views.detalles_persona, name='detalles_persona'),
    path('persona_nueva', views.persona_nueva, name="persona_nueva"),
    path('persona_actualizar/<int:pk>', views.persona_actualizar, name="persona_actualizar"),
    path('persona_eliminar/<int:pk>', views.persona_eliminar, name="persona_eliminar"),
    path('detalles_por_rut/<str:un_rut>', views.detalles_por_rut, name='detalles_por_rut'),
    path('buscar_por_rut', views.buscar_por_rut, name='buscar_por_rut'),
    path('persona_agregar_telefono/<int:pk>', views.persona_agregar_telefono, name="persona_agregar_telefono"),
    path('crear_solicitud_reserva', views.crear_solicitud_reserva, name='crear_solicitud_reserva'),
    path('persona_login', views.persona_login, name='persona_login'),
    path('persona_logout', views.persona_logout, name='persona_logout'),
    path('persona_crear_hash', views.persona_crear_hash, name='persona_crear_hash'),
]