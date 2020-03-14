# -*- coding: utf-8 -*-
"""
context_processor for common(setting)

除setting外的其他context_processor内容，均采用组件的方式(string)
"""
from django.conf import settings
import datetime


def mysetting(request):
    return {
        # 静态资源
        'STATIC_URL': settings.STATIC_URL,
        # 当前页面，主要为了login_required做跳转用
        'APP_PATH': request.get_full_path(),
        'NOW': datetime.datetime.now(),
    }
