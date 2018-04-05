# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/4/5 下午3:13'

import xadmin
from .models import UserAsk, UserCourse, UserMessage, CourseComments ,UserFavorite


class UserAskAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['name', 'mobile', 'course_name', 'add_time']

    # 增加查询功能
    search_fields = ['name', 'mobile', 'course_name']

    # 筛选字段
    list_filter = ['name', 'mobile', 'course_name', 'add_time']

class UserCourseAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['user', 'course', 'add_time']

    # 增加查询功能
    search_fields = ['user', 'course']

    # 筛选字段
    list_filter = ['user', 'course', 'add_time']

class UserMessageAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['user', 'message','has_read', 'add_time']

    # 增加查询功能
    search_fields = ['user', 'message','has_read']

    # 筛选字段
    list_filter = ['user', 'message','has_read', 'add_time']


class CourseCommentsAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['user', 'course', 'comments', 'add_time']

    # 增加查询功能
    search_fields = ['user', 'course','comments']

    # 筛选字段
    list_filter = ['user', 'course', 'comments', 'add_time']

class UserFavoriteAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['user', 'fav_id', 'fav_type','add_time']

    # 增加查询功能
    search_fields = ['user', 'fav_id', 'fav_type']

    # 筛选字段
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']

# 注册
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
