from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Author, Order


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, write_only = True)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('username', 'email', 'password' )
    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists(): 
            raise serializers.ValidationError({'email':('Email is already used')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('author', 'name','price')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.StringRelatedField(many=True)
    count_books = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ('name', 'books', 'count_books')
    def get_count_books(self, obj):
        return obj.books.count()

class OrderSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=255)
    comment = serializers.CharField(max_length=255)
    order_date = serializers.DateTimeField()
    class Meta:
        model = Order
        fields = ('book', 'user', 'phone', 'comment', 'order_date')
        lookup_field = 'book'
    def validate(self, attrs):
        book_name = attrs.get('book','')
        print(book_name.name)
        if Book.objects.filter(name=book_name.name).exists(): 
            return super().validate(attrs)
        raise serializers.ValidationError({'book':('no book with this name sorry')})

