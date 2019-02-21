from django.db import models
from django import forms
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)

    def __str__(self):
        return self.title

class FileUploadForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=2, required=True, label="名称：")
    my_file = forms.CharField(label="文件名称")

