# Generated by Django 5.0.3 on 2024-03-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_emailverifycode_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(help_text='角色', related_name='role_id', to='user.role', verbose_name='角色'),
        ),
    ]