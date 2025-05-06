from rest_framework import serializers
from rest_framework.views import APIView

from news.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


