#/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "DongChunlei"
# __date__ = "2018-06-03 21:29"
from rest_framework.viewsets import ModelViewSet
from ..models import Article
from ..serializers_class.article_serializer import ArticleModelSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer