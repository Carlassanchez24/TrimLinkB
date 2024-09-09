from rest_framework import serializers
from .models import URL
import pyshorteners


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['original_url', 'shortened_url']

    # Sobreescribimos el método `create` para acortar la URL antes de guardarla
    def create(self, validated_data):
        original_url = validated_data.get('original_url')

        # Usamos pyshorteners para acortar la URL
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(original_url)

        # Actualizamos validated_data con la URL acortada
        validated_data['shortened_url'] = shortened_url

        # Creamos y retornamos la instancia de URL con los datos validados
        return super().create(validated_data)
