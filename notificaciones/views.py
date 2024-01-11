# notificaciones/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Notificacion


@csrf_exempt  # Solo para fines demostrativos, en producción usa protección CSRF
def crear_notificacion(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        leido = request.POST.get('leido', False)
        
        notificacion = Notificacion.objects.create(mensaje=mensaje, leido=leido)
        
        return JsonResponse({'id': notificacion.id, 'mensaje': notificacion.mensaje, 'leido': notificacion.leido})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    
def listar_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    data = [{'id': notif.id, 'mensaje': notif.mensaje, 'leido': notif.leido} for notif in notificaciones]
    return JsonResponse(data, safe=False)


def eliminar_notificacion(request, notif_id):
    notificacion = get_object_or_404(Notificacion, id=notif_id)
    notificacion.delete()
    return JsonResponse({'mensaje': 'Notificación eliminada correctamente'})


def actualizar_leido(request, notif_id):
    notificacion = get_object_or_404(Notificacion, id=notif_id)
    notificacion.leido = True
    notificacion.save()
    return JsonResponse({'mensaje': 'Estatus leído actualizado correctamente'})


@csrf_exempt  # Solo para fines demostrativos, en producción usa protección CSRF
def actualizar_leido_en_lote(request):
    if request.method == 'POST':
        notif_ids = request.POST.getlist('ids[]')
        Notificacion.objects.filter(id__in=notif_ids).update(leido=True)
        return JsonResponse({'mensaje': 'Estatus leído actualizado en lote correctamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def lista_resumen_notificaciones(request):
    notificaciones_resumen = Notificacion.objects.values('id', 'leido')
    return JsonResponse(list(notificaciones_resumen), safe=False)


def contador_mensajes_por_leer(request):
    mensajes_por_leer = Notificacion.objects.filter(leido=False).count()
    return JsonResponse({'contador': mensajes_por_leer})
