from django.contrib import admin

from news.models import ArticleTranslation


@admin.register(ArticleTranslation)
class ArticleTranslationAdmin(admin.ModelAdmin):
    list_display = ("article", "language", "translated_at")
    search_fields = ("article__title", "language")