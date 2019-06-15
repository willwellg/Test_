from django.db import models
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name= '标题', max_length = 200)
    text = RichTextUploadingField('内容')
    author = models.CharField(verbose_name= '作者', max_length = 200)
    add_time = models.DateTimeField(verbose_name='创建时间', auto_now_add= True)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now= True)
    views = models.PositiveIntegerField('浏览量', default=0)
    category = models.ForeignKey('Category', verbose_name= '分类', blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name= '标签',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    #标签名
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Category(models.Model):
    #分类名
    name = models.CharField(max_length= 100)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

