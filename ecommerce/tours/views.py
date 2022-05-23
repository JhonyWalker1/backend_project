from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

# Create your views here.

from .models import Cliente,Region,Tour,Compra

from .serializers import ClienteSerializer,RegionSerializer,TourSerializer,CompraSerializer

class IndexView(APIView):
    """ permission_classes = (IsAuthenticated,) """
    def get(self,request):
        context = {
            'ok':True,
            'message':'Bienvenido a la API de Tours'
        }
        return Response(context)
    
class RegionView(APIView):
    """ permission_classes = (IsAuthenticated,) """
    def get(self,request):
        dataRegion = Region.objects.all()
        serRegion = RegionSerializer(dataRegion,many=True)
        context = {
            'ok':True,
            'content':serRegion.data
        }
        return Response(context)