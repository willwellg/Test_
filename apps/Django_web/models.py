from django.db import models
from django import forms
from ckeditor.fields import RichTextField
import django.utils.timezone as timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name= '标题', max_length = 200)
    # text = UEditorField(u'内容	',width=800, height=450, toolbars="full", imagePath="image/",
    #                     filePath="file/", upload_settings={"imageMaxSize":1204000},
    #          settings={},command=None, blank=True)
    text = RichTextField('内容')
    author = models.CharField(verbose_name= '作者', max_length = 200)
    add_time = models.DateTimeField(verbose_name='创建时间', default= timezone.now())
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now= True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = verbose_name


class FileUploadForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=2, required=True, label="名称：")
    my_file = forms.CharField(label="文件名称")

