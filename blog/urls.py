from django.urls import path
from django.views.generic import DetailView, RedirectView

from . import models
from . import views
from .views import CategoriesDetailView

urlpatterns = [
    path('test/', views.say_hello),
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:pk>/', CategoriesDetailView.as_view(pattern_name='articles_list'), name='redirect_to_category'),
    path('articles/', views.ArticlesListView.as_view(), name='articles_list'),
    path('articles/<int:pk>/', views.ArticlesDetailView.as_view(), name='redirect_to_article'),
    path('red/', RedirectView.as_view(url='https://www.youtube.com/'), name='go_to_youtube'),

]