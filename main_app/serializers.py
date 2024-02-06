from rest_framework import serializers
from .models import Planet, Moon


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'


class MoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moon
        fields = '__all__'
        read_only_fields = ('planet_id',)
