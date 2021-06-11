from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name="lista_personas"),
    path('detalles/<int:pk>', views.detalles_persona, name='detalles_persona'),
    path('persona_nueva', views.persona_nueva, name="persona_nueva"),
    path('persona_actualizar/<int:pk>', views.persona_actualizar, name="persona_actualizar"),
    path('persona_eliminar/<int:pk>', views.persona_eliminar, name="persona_eliminar"),
]