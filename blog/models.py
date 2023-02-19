from django.db import models


class Category(models.Model):
    """ Describing categories of articles on blog"""
    name = models.CharField(max_length=30, unique=True)


class Article(models.Model):
    """ Describing articles on blog"""
    title = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    content = models.TextField()
    creation_datetime = models.DateTimeField(auto_now_add=True)


