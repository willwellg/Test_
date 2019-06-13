import xadmin
from .models import Article

class ArticleAdmin(object):
    list_display = ['title', 'text', 'author', 'add_time', 'modify_time']
    list_editable = ['title', 'text', 'author', 'modify_time']
    search_field = ['title', 'author', 'modify_time']
    list_filter = ['title', 'text', 'author', 'add_time', 'modify_time']
    # style_fields = {'text': 'ueditor'}

xadmin.site.register(Article, ArticleAdmin)