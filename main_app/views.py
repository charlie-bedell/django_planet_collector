from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PlanetSerializer
from .models import Planet


# Create your views here.

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the planet-collector api home route!'}
        return Response(content)


class PlanetList(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class PlanetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    lookup_field = 'id'
