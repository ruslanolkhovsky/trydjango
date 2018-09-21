from django.http import Http404
from django.urls import reverse

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Article
from .forms import ArticleModelForm

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

# Create your views here.

# An example of Class based Views
#
#

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all() # by default looks for a specific template <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    # queryset = Article.objects.all() # by default looks for a specific template <blog>/<modelname>_list.html
    # success_url = '/'     # to override the path to go in case of success

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # Another option of how to override the default path to go in case of success
    # def get_success_url(self):
    #     return reverse('blog:article-list')


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    # queryset = Article.objects.all() # by default looks for a specific template <blog>/<modelname>_list.html
    # success_url = '/'     # to override the path to go in case of success

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article-list')
