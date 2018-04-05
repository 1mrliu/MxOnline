# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/4/5 下午2:57'

import xadmin


from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):

    # 在后台显示数据表的列名
    list_display = ['name','desc','add_time']

    # 增加查询功能
    search_fields = ['name','desc']

    # 筛选字段
    list_filter = ['name','desc', 'add_time']

class CourseOrgAdmin(object):

    # 在后台显示数据表的列名
    list_display = ['name', 'desc', 'click_num', 'fav_num','image','address','city','add_time']

    # 增加查询功能
    search_fields = ['name', 'desc', 'click_num', 'fav_num','image','address','city']

    # 筛选字段
    list_filter = ['name', 'desc', 'click_num', 'fav_num','image','address','city', 'add_time']


class TeacherAdmin(object):
    # 在后台显示数据表的列名
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']

    # 增加查询功能
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']

    # 筛选字段
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                   'add_time']


# 注册
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)