# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JSONResponse(books_serializer.data)
    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=game_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JSONResponse(book_serializer.data,
            status=status.HTTP_201_CREATED)
        return JSONResponse(book_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return JSONResponse(book_serializer.data)
    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        book_serializer = GameSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JSONResponse(book_serializer.data)
        return JSONResponse(book_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
