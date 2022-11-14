from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category, Varet, Art


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):



    class Meta:
        model = Post
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = User
#         fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = "__all__"

        # def likes_count(self):
        #     return self..all().count()


class VaretSerializer(serializers.ModelSerializer):

    class Meta:
        model = Varet
        fields = ('posts', 'author', 'content', 'name', )



class Catserializers(serializers.ModelSerializer):

    class Meta:
        model = Art
        fields = "__all__"