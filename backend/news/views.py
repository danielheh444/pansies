from rest_framework.response import Response
from rest_framework.views import APIView

from homepage.models import Preview
from news.models import ArticleTranslation
from news.translation import translate_text_yandex

class TranslateArticleView(APIView):
    def post(self, request, pk):
        article = Preview.objects.get(pk=pk)
        target_lang = request.data.get('lang')
        translation = ArticleTranslation.objects.filter(article=article, language=target_lang).first()
        if translation:
            return Response({
                "language": target_lang,
                "text": translation.text,
                "cached": True
            })

        translated_text = translate_text_yandex(article.content, target_lang)

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