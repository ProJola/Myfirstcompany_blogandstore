from django.db import models

# Create your models here.


class UserData(models.Model):
    """ Describing user data"""
    login = models.EmailField(max_length=30, help_text='E-mail', primary_key=True)
    password = models.CharField(max_length=30, help_text='Password')
    first_name = models.CharField(max_length=30, help_text='Imię')
    last_name = models.CharField(max_length=30, help_text='Nazwisko')
    date_of_birth = models.DateField(help_text="Data urodzenia")
    status = (('A', 'ACTIVE'), ('I', 'INACTIVE'))


class Category(models.Model):
    """ Describing categories of articles on blog"""
    name = models.CharField(max_length=30, unique=True)


class Article(models.Model):
    """ Describing articles on blog"""
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    article = models.TextField()
    creation_datetime = models.DateTimeField(auto_now_add=True)


