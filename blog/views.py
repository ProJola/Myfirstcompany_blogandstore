from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, RedirectView, \
    TemplateView

from blog.models import Category, Article


def say_hello(request):
    return render(request, 'blog/base.html')


class CategoriesListView(ListView):
    model = Category
    fields = '__all__'
    template_name = 'blog/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticlesListView(ListView):
    model = Article
    fields = '__all__'
    template_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoriesDetailView(RedirectView):
    pattern_name = 'articles_list'

    def get_redirect_url(self, *args, **kwargs):
        detail = get_object_or_404(Category, pk=kwargs['pk'])
        detail.update_counter()
        return super().get_redirect_url(*args, **kwargs)


class ArticlesDetailView(TemplateView):
    template_name = 'article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return context








