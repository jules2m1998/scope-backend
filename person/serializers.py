from person.models import Person, Image
from rest_framework import serializers


# Classe de sérialisation des personnes pour le model JSON
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


# Classe de érialisation des images pour le model JSON
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
