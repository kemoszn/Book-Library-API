# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from books.serializers import UserSerializer
from books.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import ScopedRateThrottle
#from rest_framework import filters
#from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'Authors': reverse(AuthorList.name, request=request),
            'Categories': reverse(CategoryList.name,
            request=request),
            'Books': reverse(BookList.name, request=request),
            'users': reverse(UserList.name, request=request),
            })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['^name']
    ordering_fields = ['name']

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'
    throttling_scope = "categories"
    throttling_classes = (ScopedRateThrottle,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['^name']
    ordering_fields = ['name']

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'
    throttling_scope = "categories"
    throttling_classes = (ScopedRateThrottle,)

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    def perform_create(self, serializer):
        # To Set the owner to the user received in request
        serializer.save(owner=self.request.user)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title','author','category','owner']
    search_fields = ['^title','^author']
    ordering_fields = ['title', 'author']

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-list'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['^name']
    ordering_fields = ['name']

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'
