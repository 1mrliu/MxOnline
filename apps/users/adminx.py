# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/4/5 下午2:06'

# 注册xadmin的model
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner

# 选择主题的功能
class BaseSetting(object):
    enable_themes = True # 主题功能
    use_bootswatch = True

# 修改后台主界面名称
class GlobalSettings(object):
    site_title = '我学后台管理'# 左上角标题名称
    site_footer = '小诺在线教育'# 底部在线名称
    menu_style = 'accordion' # 收缩左侧功能栏

class EmailVerifyRecordAdmin(object):

    # 在后台显示数据表的列名
    list_display = ['code', 'email', 'sen_type', 'sen_time']

    # 增加查询功能
    search_fields = ['code', 'email', 'sen_type']

    #筛选字段
    list_filter = ['code', 'email', 'sen_type', 'sen_time']

class BannerAdmin(object):

    # 在后台显示数据表的列名
    list_display = ['title', 'image', 'url', 'index', 'add_time']

    # 增加查询功能
    search_fields = ['title', 'image', 'url', 'index']

    # 筛选字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)