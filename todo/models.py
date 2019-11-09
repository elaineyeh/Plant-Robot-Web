import os
import time

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def mainsite_directory_path(instance, filename):
    # return 'mainsite/{}/{}'.format(instance.id, filename)
    return os.path.join('todo', str(time.time()), filename)


class Category(models.Model):
    name = models.CharField('類別', max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '類別'
        verbose_name_plural = '類別'


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name='類別')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='使用者',
                                blank=True, null=True, default=None)
    title = models.CharField('題目', max_length=64)
    body = models.TextField('文章', max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField('圖片', upload_to=mainsite_directory_path,
                              null=True, default=None)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
