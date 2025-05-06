from django.shortcuts import render
from rest_framework import viewsets

from news.models import Article
from news.serializers import ArticleSerializer


class ArticleApi(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get']