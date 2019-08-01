from rest_framework import serializers
from .models import *
from .views import *

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
    slug_field='name') #to show name of category instead of id

    class Meta:
        model = Book
        fields = ('id',
                    'title',
                    'author',
                    'category',
                    'price',
                    'in_stock',
                    'quantity',
                    'url'
        )

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
                    many=True,
                    read_only=True,
                     view_name='book-detail') #many to one relationship
    class Meta:
        model = Category
        fields = (
            'url',
            'pk',
            'name',
            'books',
        )


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
                    many=True,
                    read_only=True,
                     view_name='book-detail')

    class Meta:
        model = Author
        fields = (
                'url',
                'name',
                'books',
        )
