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
        org_nums = all_orgs.count()
        # 城市
        all_citys = CityDict.objects.all()

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
        })