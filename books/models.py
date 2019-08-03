# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, blank=False, default='',unique=True)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    quantity = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)


    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
