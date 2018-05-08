# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/5/8 下午5:18'
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
