from django.db import models

class Article(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='article_image')
