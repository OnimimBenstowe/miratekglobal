from rest_framework.serializers import ModelSerializer
from . models import *

class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'