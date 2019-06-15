import xadmin
from xadmin import views
from .models import Article, Tag, Category

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
    list_display = ['title', 'text', 'author', 'add_time', 'modify_time', 'views', 'tags', 'category' ]
    list_editable = ['title', 'author', 'modify_time', 'category']
    search_field = ['title', 'author', 'modify_time', 'views', 'tags', 'category']
    list_filter = ['title', 'text', 'author', 'add_time', 'modify_time', 'views', 'tags', 'category']

class TagAdmin(object):
    list_display = ['name']
    list_editable = ['name']
    search_field = ['name']
    list_filter = ['name']

class CategoryAdmin(object):
    list_display = ['name', 'parent_category']
    list_editable = ['name', 'parent_category']
    search_field = ['name', 'parent_category']
    list_filter = ['name', 'parent_category']
    
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)