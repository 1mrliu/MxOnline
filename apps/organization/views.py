# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class OrgView(View):
    '''
    课程机构列表功能
    '''
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 热门机构的提取
        hot_orgs = all_orgs.order_by("click_num")[:3]

        # 城市
        all_citys = CityDict.objects.all()

        # 去除筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get ('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students") #  - 倒叙排序
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        org_nums = all_orgs.count ()
        # 对课程机构进行分页
        try:
            page = request.GET.get ('page', 1)
        except PageNotAnInteger:
            page = 1
        # 必须设置每页显示的数量 per_page的值
        p = Paginator(all_orgs, 3,request=request)

        orgs = p.page (page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id":city_id, # 传递city_id到templates中
            "category":category,
            "hot_orgs":hot_orgs,
            "sort":sort,
        })