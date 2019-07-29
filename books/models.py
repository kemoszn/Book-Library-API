# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    quantity = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=100, blank=False)

    if quantity == 0:
        in_stock = False
    else:
        in_stock = True


    class Meta:
        ordering = ('title',)
