

from rest_framework import serializers

from books_api.models import Book, Author, Publisher

'''
class BookSerializer(serializers.Serializer):

    title = serializers.CharField()

    description = serializers.CharField(
        max_length = 100
    )

    pages = serializers.IntegerField()

    author = serializers.CharField()''

'''

class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):

    author = SimpleAuthorSerializer(many=True)

    class Meta:
        model = Book
        fields='__all__'

    def create(self,validated_data):

       authors = [a.get('name') for a in validated_data.pop('author')]
       book = Book.objects.create(**validated_data)
       existing_authors = Author.objects.filter(name__in=authors)
       new_authors = list(set(authors) - set(a.name for a in existing_authors))
       created_authors = Author.objects.bulk_create([Author(name=name) for name in new_authors])
       all_authors = list(existing_authors) + created_authors
       book.author.add(*all_authors)
       return book

    def update(self,instance,validated_data):

        m2m_field = validated_data.pop('author',None)

        for key,value in validated_data.items():
            setattr(instance,key,value)

        instance.save()
        authors = []
        if m2m_field:

            for author_data in m2m_field :
                author,_ = Author.objects.get_or_create(**author_data)
                authors.append(author)

            instance.author.set(authors)
        else:
            instance.author.set(authors)

        return instance


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class HyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

