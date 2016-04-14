#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
根据json生成private String 属性;
数据源必须是没有经过null过滤的.
"""
import re
s="""

03-17 16:28:51.782: E/(29560): {"message":"\u83b7\u53d6\u6210\u5,"available_balance":null}]}


"""
ss=re.findall(r'(?<!:)"([.\w]*?)"',s)
for s in ss:
    print("private String %s;" % s)
