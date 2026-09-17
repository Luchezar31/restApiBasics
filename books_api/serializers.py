

from rest_framework import serializers

from books_api.models import Book


'''
class BookSerializer(serializers.Serializer):

    title = serializers.CharField()

    description = serializers.CharField(
        max_length = 100
    )

    pages = serializers.IntegerField()

    author = serializers.CharField()''

'''

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields='__all__'