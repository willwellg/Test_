from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import *

# Create your views here.
class ArticleListView(ListView):
    model = Article
    paginate_by = settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE

    def get_queryset(self):
        article_list = Article.objects.all().order_by("-modify_time")
        return article_list

class ArticleDetailView(DetailView):
    model = Article

    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

class TagView(ListView):
    model = Article
    context_object_name = 'article_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk = self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags = tag)








