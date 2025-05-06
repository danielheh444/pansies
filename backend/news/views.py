from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import Article, ArticleTranslation
from news.serializers import ArticleSerializer
from news.translation import translate_text_yandex


class ArticleApi(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get']


class TranslateArticleView(APIView):
    def post(self, request, pk):
        article = Article.objects.get(pk=pk)
        target_lang = request.data.get('lang')
        translation = ArticleTranslation.objects.filter(article=article, language=target_lang).first()
        if translation:
            return Response({
                "language": target_lang,
                "text": translation.text,
                "cached": True
            })

        translated_text = translate_text_yandex(article.text, target_lang)

        new_translations = ArticleTranslation.objects.create(
            article=article,
            language=target_lang,
            text=translated_text
        )

        return Response({
            "language": target_lang,
            "text": new_translations.text,
            "cached": False
        })