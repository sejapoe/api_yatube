from rest_framework.serializers import ModelSerializer, StringRelatedField

from posts.models import Post, Comment, Group


class PostSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date', 'image', 'group')
        read_only_fields = ('id', 'author', 'pub_date')


class CommentSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('id', 'author', 'post', 'created')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        read_only_fields = ('id', 'title', 'slug', 'description')
