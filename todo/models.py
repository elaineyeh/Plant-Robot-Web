from django.db import models
from django.utils import timezone
import os
import time

# Create your models here.

def mainsite_directory_path(instance, filename):
    # return 'mainsite/{}/{}'.format(instance.id, filename)
    return os.path.join('mainsite', str(time.time()), filename)

class Category(models.Model):
    name = models.CharField('類別', max_length = 10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '類別'
        verbose_name_plural = '類別'

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='類別')
    title = models.CharField('題目', max_length=64)
    body = models.CharField('文章', max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
