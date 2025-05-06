from django.contrib import admin

from news.models import Article, ArticleTranslation

admin.site.register(Article)
admin.site.register(ArticleTranslation)
