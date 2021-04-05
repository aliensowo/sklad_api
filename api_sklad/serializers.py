from rest_framework import serializers
from .models import Resources


class ResourcesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обработки данных со всеми полями
    """
    class Meta:
        model = Resources
        fields = ('id', 'title', 'amount', 'unit', 'price', 'date', )


class PostResourcesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обраотки полей 'title', 'amount', 'unit', 'price', 'date'
    """
    class Meta:
        model = Resources
        fields = ('title', 'amount', 'unit', 'price', 'date')
