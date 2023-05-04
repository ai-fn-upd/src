from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for the movie model
    """
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'preview', 'likes')

