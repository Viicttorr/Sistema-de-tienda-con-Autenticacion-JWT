from rest_framework.response import Response
from rest_framework.decorators import api_view
from productos.models import Producto
import random
from .serializador import ProductoSerializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_productos(request):
    personas = Producto.objects.all()
    serializer = ProductoSerializers(personas, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_producto_random(request):
    total = Producto.objects.count() #cuenta personas en la base
    indice = random.randint(0, total - 1) #número aleatorio entre 0 y total-1
    producto = Producto.objects.all()[indice] #obtiene la persona del indice
    serializer = ProductoSerializers(producto, many=False)
    return Response(serializer.data)