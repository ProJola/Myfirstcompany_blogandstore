from django.urls import path
from . import models
from . import views

urlpatterns = [
    path('test/', views.say_hello),
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
]