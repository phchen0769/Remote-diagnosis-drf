# Generated by Django 5.0.3 on 2024-03-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(default='https://m.imooc.com/static/wap/static/common/img/logo-small@2x.png', help_text='用户头像', max_length=50, verbose_name='用户头像'),
        ),
    ]
