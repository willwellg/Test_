# Generated by Django 2.1.7 on 2019-05-17 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Django_web', '0004_remove_article_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 17, 8, 10, 1, 73829, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]