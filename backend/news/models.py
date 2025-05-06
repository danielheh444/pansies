from django.db import models

class Article(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='article_image')


class ArticleTranslation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10)
    text = models.TextField()
    translated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('article', 'language')