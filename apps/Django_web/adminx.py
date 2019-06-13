import xadmin
from xadmin import views
from .models import Article

class BaseSetting:
    """
    主题设置
    """
    enable_themes = True
    use_bootswatch = True

class GlobalSettings:
    """
    后台修改
    """
    site_title = 'willwellg'
    site_footer = 'willwellg@2019'
    menu_style = 'accordion'  # 开启分组折叠



class ArticleAdmin(object):
    list_display = ['title', 'text', 'author', 'add_time', 'modify_time']
    list_editable = ['title', 'text', 'author', 'modify_time']
    search_field = ['title', 'author', 'modify_time']
    list_filter = ['title', 'text', 'author', 'add_time', 'modify_time']
    # style_fields = {'text': 'ueditor'}

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Article, ArticleAdmin)