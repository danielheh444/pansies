from django.db import models

from homepage.models import Preview


class ArticleTranslation(models.Model):
    article = models.ForeignKey(Preview, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10)
    text = models.TextField()
    translated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('article', 'language')