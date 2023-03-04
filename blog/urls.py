from django.urls import path
from django.views.generic import DetailView, RedirectView

from . import models
from . import views
from .views import CategoriesDetailView

urlpatterns = [
    path('test/', views.say_hello),
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:pk>/', CategoriesDetailView.as_view(), name='categories_detail'),
    path('articles/', views.ArticlesListView.as_view(), name='articles_list'),
    path('red/', RedirectView.as_view(url='https://www.youtube.com/'), name='go_to_youtube'),

]