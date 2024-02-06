from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PlanetSerializer, MoonSerializer
from .models import Planet, Moon


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


class MoonListCreate(generics.ListCreateAPIView):
    serializer_class = MoonSerializer

    def get_queryset(self):
        planet_id = self.kwargs['planet_id']
        return Moon.objects.filter(planet_id=planet_id)

    def perform_create(self, serializer):
        planet_id = self.kwargs['planet_id']
        planet = Planet.objects.get(id=planet_id)
        serializer.save(planet=planet)


class MoonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoonSerializer
    lookup_field = 'id'

    def get_queryset(self):
        planet_id = self.kwargs['planet_id']
        return Moon.objects.filter(planet_id=planet_id)
