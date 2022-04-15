from rest_framework import serializers
from books.books_api.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    # Custom validator

    # Variant 1
    # def validate(self, data):
    #     title = data['title']
    #     if title:
    #         start_letter = title[0]
    #         if not start_letter.isupper():
    #             raise serializers.ValidationError('Title must start with capital')
    #         return data

    # Variant 2
    def validate(self, data):
        if data.get('title'):
            if not data.get('title')[0].isupper():
                raise serializers.ValidationError('Title must start with capital')
            return data

    class Meta:
        model = BookModel
        fields = '__all__'
