from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from books_api.models import Book
from books_api.serializers import BookSerializer


'''
@api_view(['GET','POST','PUT','DELETE'])
def book(request, pk):
    book = get_object_or_404(Book,pk=pk)
    serializer = BookSerializer(book)

    if request.method=="DELETE":
        book.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method=="GET":
        return Response(serializer.data,status=status.HTTP_200_OK)

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data

        book,created = Book.objects.update_or_create(
            title=data['title'],
            pages=data['pages'],
            description=data['description'],
            author=data['author']
        )
        output_serializer = BookSerializer(book)
        return Response(data=output_serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(output_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
'''

@api_view(['GET','POST','PUT','DELETE'])
def book(request, pk):
    book = get_object_or_404(Book,pk=pk)
    serializer = BookSerializer(book)

    if request.method=="DELETE":
        book.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method=="GET":
        return Response(serializer.data,status=status.HTTP_200_OK)

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data

        book,created = Book.objects.update_or_create(
            pk=pk,
            defaults={
                'title':data['title'],
                'pages':data['pages'],
                'description':data['description'],
                'author':data['author']
            }
        )
        output_serializer = BookSerializer(book)
        return Response(data=output_serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)