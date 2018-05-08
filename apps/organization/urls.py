# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/5/8 下午7:59'
# 存放所有课程目录下的url配置
from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask")
]