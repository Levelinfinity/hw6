from rest_framework import serializers

from .models import Books, Library


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ("id", "title", "author", "price")
        read_only_fields = ("id",)


class LibrarySerializer(serializers.ModelSerializer):
    books = BooksSerializers(many=True, read_only=True)

    class Meta:
        Model = Library 
        fields = ['id', 'name', 'address', 'city', 'books']
