#!usr/bin/env python  
# -*- coding:utf-8 _*-  
# @author:jinke
# @file: views.py 
# @version:
# @time: 2020/03/14
from django.shortcuts import render


def dashboard(request):
    """
    首页
    :param request:
    :return:
    """

    return render(request, 'dashboard.html')