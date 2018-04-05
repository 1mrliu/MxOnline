# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/4/5 下午2:37'

from .models import Course, Lesson, Video, CourseResource
import xadmin

class CourseAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums','image', 'click_nums', 'add_time']
    # 增加查询功能
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums','image', 'click_nums']

    # 筛选字段
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums','image', 'click_nums', 'add_time']


class LessonAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['course', 'name', 'add_time']

    # 增加查询功能
    search_fields = ['course', 'name']

    # 筛选字段
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['lesson', 'name', 'add_time']

    # 增加查询功能
    search_fields = ['lesson', 'name']

    # 筛选字段  搜索课程名__name
    list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['course', 'name', 'download', 'add_time']

    # 增加查询功能
    search_fields = ['course', 'name', 'download']

    # 筛选字段  搜索课程名__name
    list_filter = ['course', 'name', 'download', 'add_time']


# 注册
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)