from rest_framework import serializers
from .models import *
from .views import *
from django.contrib.auth.models import User


class UserBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: #Serializes all books related to the User
        model = Book
        fields = (
        'url',
        'name'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = UserBookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
        'url',
        'pk',
        'username',
        'games'
        )

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    author = serializers.SlugRelatedField(queryset=Author.objects.all(),
    slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
    slug_field='name') #to show name of category instead of id

    class Meta:
        model = Book
        depth = 4
        fields = ('id',
                    'owner',
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
