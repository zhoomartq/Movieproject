from rest_framework import serializers
from .models import Category, Movie, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'category', 'author', 'created_at', 'text')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = PostImageSerializer(instance.images.all(),many=True, context=self.context).data
        return representation


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'