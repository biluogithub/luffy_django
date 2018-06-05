#/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "DongChunlei"
# __date__ = "2018-06-01 20:09"
from django.conf.urls import url
from .views.course_view import CourseViewSet,CourseDetailViewSet
from .views.article_view import ArticleViewSet



urlpatterns = [
    # 课程API：获取所有课程数据 & 发送POST请求创建课程
    url(r'course/$', CourseViewSet.as_view({'get':'list','post':'create'})),
    # 课程API：获取单条课程数据 & 更新单条课程数据 & 删除单条课程数据
    url(r'course/(?P<pk>\d+)/', CourseViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy','patch':'partial_update'})),

    # 课程详细API：获取所有课程详细数据 & 发送POST请求创建课程详细
    url(r'course_detail/$', CourseDetailViewSet.as_view({'get':'list','post':'create'})),
    # 课程详细API：获取单条课程详细信息 & 更新单条课程详细信息 & 删除单条课程详细信息
    url(r'course_detail/(?P<pk>\d+)/', CourseDetailViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    url(r'article/$', ArticleViewSet.as_view({'get':'list','post':'create'})),

]