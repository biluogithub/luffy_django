#/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "DongChunlei"
# __date__ = "2018-06-01 20:25"
from rest_framework import serializers
from ..models import Course,CourseDetail


class CourseModelSerializer(serializers.ModelSerializer):
    '''序列化课程'''
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailModelSerializer(serializers.ModelSerializer):
    '''序列化课程详细'''

    # Course相关
    name = serializers.CharField(source='course.name')
    course_img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')
    brief = serializers.CharField(source='course.brief')

    # 价格策略部分在课程概览中展示

    # 在"我将学到哪些内容"部分加入"课程大纲"表
    outline = serializers.SerializerMethodField()

    def get_outline(self, obj):
        """
        获取课程大纲表
        :param obj:
        :return:
        """
        queryset = obj.courseoutline_set.all()
        return [{'title': row.title, 'content': row.content} for row in queryset]

    # CourseDetail相关：推荐课程M2M
    recommend_courses = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    def get_recommend_courses(self, obj):
        queryset = obj.recommend_courses.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]

    def get_teachers(self, obj):
        queryset = obj.teachers.all()
        return [{'teacher_name': i.name, 'teacher_title': i.title, 'teacher_brief': i.brief} for i in queryset]

    # CourseChapter相关：课程章节、课程目录(跨两张表)
    chapter = serializers.SerializerMethodField()

    def get_chapter(self, obj):
        queryset = obj.course.coursechapters.all()

        return [{'chapter_name': i.name, 'chapter_chapter': i.chapter,
                 'chapter_summary': i.summary, 'chapter_date': i.pub_date,
                 'sections':
                     [{'section_name': j.name, 'section_video_time': j.video_time,
                       'section_pub_date': j.pub_date, 'sections_free_trail': j.free_trail}
                      for j in i.coursesections.all()]
                 } for i in queryset]

    class Meta:
        model = CourseDetail
        fields = ['name', 'course_img', 'level', 'brief', 'course_slogan', 'video_brief_link', 'why_study',
                  'what_to_study_brief', 'career_improvement', 'prerequisite', 'outline', 'recommend_courses',
                  'teachers', 'chapter',]
    # class Meta:
    #     model = CourseDetail
    #     fields = '__all__'