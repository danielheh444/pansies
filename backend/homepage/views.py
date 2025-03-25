from django.shortcuts import render
from rest_framework import viewsets

from homepage.models import Preview
from homepage.serializers import PreviewSerializer

class PreviewViewApi(viewsets.ModelViewSet):
    queryset = Preview.objects.all()
    serializer_class = PreviewSerializer
