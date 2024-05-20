from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializers import *
from . serializers_gallery import *

# Create your views here.
@api_view(['GET'])
def contDB(request):
    db_data = Content.objects.all()
    serialized_data = ContentSerializer(db_data, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def galleryDB(request):
    db_data = Gallery.objects.all()
    serialized_data = GallerySerializer(db_data, many=True)
    return Response(serialized_data.data)