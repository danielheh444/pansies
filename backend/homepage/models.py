from django.db import models

class Preview(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='preview_image')
    image = models.ImageField(upload_to='image', null=True)
    content = models.TextField(null=True)
