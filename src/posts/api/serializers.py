from rest_framework.serializers import ModelSerializer

from ..models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',       
            'title',
            'slug',
            'content',
            'publish'
        ]

        # To print all contents
        # fields = '__all__'