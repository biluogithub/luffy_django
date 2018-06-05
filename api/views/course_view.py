#/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "DongChunlei"
# __date__ = "2018-06-01 20:06"
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework import mixins

from ..models import Course,CourseDetail
from ..serializers_class.course_serializer import CourseModelSerializer,CourseDetailModelSerializer

class CourseViewSet(ModelViewSet):
    '''课程视图'''
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


class CourseDetailViewSet(ModelViewSet):
    '''课程详细视图'''
    from rest_framework.authentication import SessionAuthentication
    authentication_classes = []
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailModelSerializer