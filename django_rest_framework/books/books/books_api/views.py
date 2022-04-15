from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from books.books_api.models import BookModel
from books.books_api.serializers import BookSerializer


class BookListCreate(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):
    def put(self, request, pk):
        try:
            book = BookModel.objects.get(pk=pk)
            book_serializer = BookSerializer(book, data=request.data)
            if book_serializer.is_valid():
                book_serializer.save()
                return Response(book_serializer.data, status=status.HTTP_200_OK)
            return Response(book_serializer.errors)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = BookModel.objects.get(pk=pk)
        if book:
            book_serializer = BookSerializer(book)
            return Response(book_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            book = BookModel.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
