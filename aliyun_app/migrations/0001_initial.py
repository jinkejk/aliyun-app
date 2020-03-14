# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u8ba2\u5355\u53f7', blank=True)),
                ('serial_no', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('support', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('team', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('ticket_no', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('product_no', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u8d27\u53f7', blank=True)),
                ('eng_name', models.CharField(default=b'', max_length=150, null=True, verbose_name='\u82f1\u6587\u540d\u79f0', blank=True)),
                ('ch_name', models.CharField(default=b'', max_length=150, null=True, verbose_name='\u4e2d\u6587\u540d\u79f0', blank=True)),
                ('number', models.IntegerField(default=0, verbose_name='\u6570\u91cf')),
                ('sign_time', models.DateTimeField(default=b'', null=True, verbose_name='\u5408\u540c\u7b7e\u8ba2\u65e5\u671f', blank=True)),
                ('confirm_time', models.DateTimeField(default=b'', null=True, verbose_name='\u4e0b\u5355\u65e5\u671f', blank=True)),
                ('in_time', models.DateTimeField(default=b'', null=True, verbose_name='\u5165\u5e93\u65e5\u671f', blank=True)),
                ('out_time', models.DateTimeField(default=b'', null=True, verbose_name='\u51fa\u5e93\u65e5\u671f', blank=True)),
                ('install_time', models.DateTimeField(default=b'', null=True, verbose_name='\u5b89\u88c5\u65e5\u671f', blank=True)),
                ('company', models.CharField(default=b'', max_length=150, null=True, verbose_name='\u5355\u4f4d\u540d\u79f0', blank=True)),
                ('province', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u7701', blank=True)),
                ('city', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u5e02', blank=True)),
                ('street', models.CharField(default=b'', max_length=255, null=True, verbose_name='\u8857\u9053', blank=True)),
                ('contact', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u8054\u7cfb\u4eba', blank=True)),
                ('mobile', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u624b\u673a\u53f7', blank=True)),
                ('mail', models.CharField(default=b'', max_length=50, null=True, verbose_name='\u90ae\u7bb1', blank=True)),
                ('remark', models.TextField(default=b'', null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u6570\u636e',
                'verbose_name_plural': '\u8ba2\u5355\u6570\u636e',
            },
        ),
    ]
