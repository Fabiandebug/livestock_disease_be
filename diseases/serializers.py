from rest_framework import serializers
from .models import disease, image


# Image Serilizer
class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = "__all__"


# disease serializer
class diseaseSerializer(serializers.ModelSerializer):
    images = imageSerializer(many=True, read_only=True)

    class Meta:
        model = disease
        fields = "__all__"
