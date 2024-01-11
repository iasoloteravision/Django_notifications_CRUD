# notificaciones/urls.py
from django.urls import path
from .views import listar_notificaciones, eliminar_notificacion, actualizar_leido, actualizar_leido_en_lote, lista_resumen_notificaciones, contador_mensajes_por_leer, crear_notificacion

urlpatterns = [
    path('listar/', listar_notificaciones, name='listar_notificaciones'),
    path('eliminar/<int:notif_id>/', eliminar_notificacion, name='eliminar_notificacion'),
    path('actualizar_leido/<int:notif_id>/', actualizar_leido, name='actualizar_leido'),
    path('actualizar_leido_en_lote/', actualizar_leido_en_lote, name='actualizar_leido_en_lote'),
    path('lista_resumen/', lista_resumen_notificaciones, name='lista_resumen_notificaciones'),
    path('contador_mensajes_por_leer/', contador_mensajes_por_leer, name='contador_mensajes_por_leer'),
    path('crear_notificacion/', crear_notificacion, name='crear_notificacion'),
]
