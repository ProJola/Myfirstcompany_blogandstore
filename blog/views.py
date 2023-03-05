from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, RedirectView, \
    TemplateView, DetailView

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


class CategoriesDetailView(DetailView):
    template_name = 'blog/categories_detail.html'
    model = Category
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticlesListView(ListView):
    template_name = 'blog/articles_list.html'
    model = Article
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context









