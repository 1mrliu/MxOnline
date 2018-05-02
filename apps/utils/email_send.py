# -*- coding: utf-8 -*-
from random import Random



__author__ = 'liudong'
__date__ = '2018/4/5 下午10:18'

from django.core.mail import send_mail

from users.models import  EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.sen_type =  send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "在线网注册链接"
        email_body = "请点击下边的链接：http://127.0.0.1：8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "在线网注册链接"
        email_body = "请点击下边的链接：http://127.0.0.1：8000/reset/{0}".format (code)

        send_status = send_mail (email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass