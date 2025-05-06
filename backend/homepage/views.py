from django.shortcuts import render
from rest_framework import viewsets

from homepage.models import Preview
from homepage.serializers import PreviewSerializer

class PreviewApi(viewsets.ModelViewSet):
    queryset = Preview.objects.all()
    serializer_class = PreviewSerializer
    http_method_names = ['get']
