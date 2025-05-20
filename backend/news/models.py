from django.db import models

from homepage.models import Preview


class ArticleTranslation(models.Model):
    article = models.ForeignKey(Preview, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10)

    translated_title = models.CharField(max_length=200)
    translated_description = models.TextField()
    translated_content = models.TextField()

    translated_at = models.DateTimeField(auto_now_add=True)




    class Meta:
        unique_together = ('article', 'language')

    def __str__(self):
        return f"{self.article.title} [{self.language}]"