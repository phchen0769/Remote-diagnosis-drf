# Generated by Django 5.0.3 on 2024-04-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_role_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='desc',
            field=models.CharField(help_text='描述', max_length=300, null=True, verbose_name='描述'),
        ),
    ]