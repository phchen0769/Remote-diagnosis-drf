# Generated by Django 5.1.2 on 2024-11-29 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(help_text='文章内容', max_length=2000, null=True, verbose_name='文章内容'),
        ),
    ]