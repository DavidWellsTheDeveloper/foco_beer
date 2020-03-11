from .models import Brewery, Beer
from rest_framework import serializers

class BreweriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brewery
        exclude = ''

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        exclude = ''
