# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Book
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'in_stock', 'author', 'quantity', 'category', 'price')

admin.site.register(Book, BookAdmin)
