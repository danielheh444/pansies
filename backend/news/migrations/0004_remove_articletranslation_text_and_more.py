# Generated by Django 5.1.3 on 2025-05-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_articletranslation_article_delete_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletranslation',
            name='text',
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='translated_content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='translated_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='translated_title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
