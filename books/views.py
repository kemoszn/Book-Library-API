# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data)
    elif request.method == 'POST':
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data,
            status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'POST'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return Response(book_serializer.data)

    elif request.method == 'PUT':
        book_serializer = GameSerializer(book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data)
        return Response(book_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
