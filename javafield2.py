#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
根据json生成private String 属性;
数据源必须是没有经过null过滤的.
"""
import re
s="""



orderId	Long	是	采购单Id		
specId	String	否	sku规格Id，例如af478130f6c683c4c77bb511796617d7，非sku类型则不用传		
specInfo	Map	否	sku规格信息的Map,key为规格属性名称，value为规格属性值，例如{"颜色":"黄色","尺码":"XS"}		
buyAmount	Long	是	购买数量

"""
ss=s.split("\n")
print(len(ss))
def get():
    for c in ss:
     cc=c.split('\t')
     if len(cc)>=3:
         print("private %s %s;"%(cc[1],cc[0]))
get()
