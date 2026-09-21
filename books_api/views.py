from functools import partial

from django.db.migrations import serializer
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
'''


class BookDetailApiViewSet(APIView):

    serializer_class = BookSerializer
        
    def get(self,request,pk=None,*args,**kwargs):

        book = Book.objects.get(pk=pk)

        serializer=self.serializer_class(book)

        response = Response(serializer.data,status.HTTP_200_OK)
        
        return response

    
    def put(self,request,pk):

        book = Book.objects.get(pk=pk)
        
        serializer = self.serializer_class(instance=book,data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status.HTTP_200_OK)

    def patch(self,request,pk):
        book = Book.objects.get(pk=pk)
        
        serializer = self.serializer_class(instance=book,data=request.data,partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status.HTTP_200_OK)

    def delete(self,request,pk):
        book = Book.objects.get(pk=pk)
        book.delete()

        return Response(status=status.HTTP_200_OK)

        


class BookCreateListApiViewSet(APIView):

    serializer_class = BookSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def get(self,request):
        books = Book.objects.all()

        serializer =self.serializer_class(books,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)