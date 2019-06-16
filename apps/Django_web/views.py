from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.
class ArticleListView(ListView):
    model = Article
    paginate_by = 2

    def get_queryset(self):
        article_list = Article.objects.all().order_by("-modify_time")
        return article_list

class ArticleDetailView(DetailView):
    model = Article






