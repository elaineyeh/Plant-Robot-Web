# Generated by Django 2.0.3 on 2019-10-10 13:28

from django.db import migrations, models
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=todo.models.mainsite_directory_path, verbose_name='圖片'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=1000, verbose_name='文章'),
        ),
    ]
