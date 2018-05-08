# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/5/8 下午5:18'

import re
from django import forms
from operation.models import UserAsk

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=5, max_length=5)


# ModelForm 比上边的Form的效果更加好
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    # 自定义的验证方式
    def clean_mobile(self):
        """
        验证手机号码是否合法 
        """
        mobile = self.cleaned_data['mobile']
        # re正则表达式
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            # 抛出异常
            raise forms.ValidationError(u"手机号码非法", code='mobile_invilable')
