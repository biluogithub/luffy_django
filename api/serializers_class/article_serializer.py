#/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "DongChunlei"
# __date__ = "2018-06-03 21:19"
from rest_framework import serializers
from ..models import Article,ArticleSource,Collection,Comment,Account,UserAuthToken


class ArticleModelSerializer(serializers.ModelSerializer):

    # 来源相关
    name = serializers.CharField(source='source.name')



    class Meta:
        model = Article
        fields = '__all__'



