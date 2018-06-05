from django.conf.urls import url, include
from api.views import course

# 星哥哥——————————————————————
urlpatterns = [
    url(r'^coursecategory/$', course.CourseCategoryView.as_view({'get': 'list'})),


    url(r'^course/$', course.CourseView.as_view({'get': 'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),
]




