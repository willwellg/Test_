from django.views.generic import ListView
from .models import *

# Create your views here.
class ArticleListView(ListView):
    model = Article
    paginate_by = 2

    def get_queryset(self):
        article_list = Article.objects.all().order_by("-modify_time")
        return article_list







