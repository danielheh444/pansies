from rest_framework.response import Response
from rest_framework.views import APIView

from homepage.models import Preview
from news.models import ArticleTranslation
from news.translation import translate_text_yandex

class TranslateArticleView(APIView):
    def post(self, request, pk):
        article = Preview.objects.get(pk=pk)
        target_lang = request.data.get('lang')

        if not target_lang:
            return Response({"error": "Language parameter 'lang' is required"}, status=400)

        translation = ArticleTranslation.objects.filter(article=article, language=target_lang).first()
        if translation:
            return Response({
                "language": target_lang,
                "title": translation.translated_title,
                "description": translation.translated_description,
                "content": translation.translated_content,
                "cached": True
            })

        translated_title = translate_text_yandex(article.title, target_lang)
        translated_description = translate_text_yandex(article.description, target_lang)
        translated_content = translate_text_yandex(article.content or "", target_lang)


        new_translations = ArticleTranslation.objects.create(
            article=article,
            language=target_lang,
            translated_title=translated_title,
            translated_description=translated_description,
            translated_content=translated_content
        )

        return Response({
            "language": target_lang,
            "title": new_translations.translated_title,
            "description": new_translations.translated_description,
            "content": new_translations.translated_content,
            "cached": False
        })