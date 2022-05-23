from rest_framework import serializers

from .models import Cliente,Region,Tour,Compra

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
class RegionTourSerializer(serializers.ModelSerializer):
    Tours = TourSerializer(many=True,read_only=True)
    class Meta:
        model = Region
        fields = ['region_id','region_nombre','Tours']