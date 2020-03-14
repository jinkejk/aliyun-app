#!usr/bin/env python  
# -*- coding:utf-8 _*-  
# @author:jinke
# @file: models.py.py 
# @version:
# @time: 2020/03/14

from django.db import models


class Record(models.Model):
    """基本记录的信息"""
    order_id = models.CharField(u'订单号', max_length=100, null=True, blank=True, default='')
    serial_no = models.CharField(max_length=100, null=True, blank=True, default='')
    support = models.CharField(max_length=100, null=True, blank=True, default='')
    team = models.CharField(max_length=100, null=True, blank=True, default='')
    ticket_no = models.CharField(max_length=100, null=True, blank=True, default='')
    product_no = models.CharField(u'货号', max_length=100, null=True, blank=True, default='')
    eng_name = models.CharField(u'英文名称', max_length=150, null=True, blank=True, default='')
    ch_name = models.CharField(u'中文名称', max_length=150, null=True, blank=True, default='')
    number = models.IntegerField(u'数量', default=0)
    sign_time = models.DateTimeField(u'合同签订日期', null=True, blank=True, default='')
    confirm_time = models.DateTimeField(u'下单日期', null=True, blank=True, default='')
    in_time = models.DateTimeField(u'入库日期', null=True, blank=True, default='')
    out_time = models.DateTimeField(u'出库日期', null=True, blank=True, default='')
    install_time = models.DateTimeField(u'安装日期', null=True, blank=True, default='')
    company = models.CharField(u'单位名称', max_length=150, null=True, blank=True, default='')
    province = models.CharField(u'省', max_length=20, null=True, blank=True, default='')
    city = models.CharField(u'市', max_length=20, null=True, blank=True, default='')
    street = models.CharField(u'街道', max_length=255, null=True, blank=True, default='')
    contact = models.CharField(u'联系人', max_length=20, null=True, blank=True, default='')
    mobile = models.CharField(u'手机号', max_length=20, null=True, blank=True, default='')
    mail = models.CharField(u'邮箱', max_length=50, null=True, blank=True, default='')
    remark = models.TextField(u'备注', null=True, blank=True, default='')

    def __unicode__(self):
        return unicode('[' + self.order_id + ']  ' + '[' + self.product_no + ']  ' + self.ch_name)

    class Meta:
        verbose_name = u'订单数据'
        verbose_name_plural = u"订单数据"
