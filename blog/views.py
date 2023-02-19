from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, ListView

from blog.models import Category


def say_hello(request):
    return render(request, 'blog/test.html')


class CategoriesListView(ListView):
    model = Category
    fields = '__all__'
    template_name = 'blog/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





