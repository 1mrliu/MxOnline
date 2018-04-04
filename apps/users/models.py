# -*- coding: utf-8 -*-
# 第一块区域是Python自带的
from __future__ import unicode_literals
from datetime import datetime
# 第二块是导入的模块
from django.db import models
from django.contrib.auth.models import  AbstractUser

#第三块是我们自定义的模块


# Create your models here.
# 继承django自带的abstractuser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default="")
    birday = models.DateField(verbose_name="生日", null=True)
    gender = models.CharField(max_length=5, choices=(('male','男'),('female','nv')),default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="iamge/default.png", max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

# 邮箱验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    sen_type = models.CharField(choices=(("register", "注册"),("forget","找回密码")), max_length=10)
    sen_time = models.DateTimeField(default=datetime.now)# 去掉括号的原因是可以让时间根据class生成的时间来进行计算

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

#轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100,verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name






