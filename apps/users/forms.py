# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/4/5 下午8:41'
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)# TRUE表示必填字段
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()

