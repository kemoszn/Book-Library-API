# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

class BookList(genrics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'

class BookDetail(generics.RetrieveUpdateDestroyAPIView:
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-list'

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail' 
