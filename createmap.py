#!/usr/bin/env python 2.7
#-*- coding:utf-8 -*-
"""
重组map
"""
import re

s="""map = new HashMap<String,String>();	map.put("value","itemNumber");map.put("label","Item Number");fields.add(map);
map = new HashMap<String,String>();	map.put("value","styleCode");map.put("label","Style Code");fields.add(map);
map = new HashMap<String,String>();	map.put("value","styleDesc");map.put("label","Style Description");fields.add(map);
map = new HashMap<String,String>();	map.put("value","colorCode");map.put("label","Color Code");fields.add(map);
map = new HashMap<String,String>();	map.put("value","colorDesc");map.put("label","Color Description");fields.add(map);
map = new HashMap<String,String>();	map.put("value","itemDimension");map.put("label","Item Dimension");fields.add(map);
map = new HashMap<String,String>();	map.put("value","itemSize");map.put("label","Item Size");fields.add(map);
map = new HashMap<String,String>();	map.put("value","itemDescription");map.put("label","Item Description");fields.add(map);
map = new HashMap<String,String>();	map.put("value","uom");map.put("label","UOM");fields.add(map);
map = new HashMap<String,String>();	map.put("value","hsNumber");map.put("label","HS Number");fields.add(map);
map = new HashMap<String,String>();	map.put("value","unitWeight");map.put("label","Unit Weight");fields.add(map);
map = new HashMap<String,String>();	map.put("value","unitWeightUom");map.put("label","Unit Weight UOM");fields.add(map);
map = new HashMap<String,String>();	map.put("value","salesPrice");map.put("label","Sales Price");fields.add(map);
map = new HashMap<String,String>();	map.put("value","retailPrice");map.put("label","Retail Price");fields.add(map);
map = new HashMap<String,String>();	map.put("value","taxPerc");map.put("label","Tax Perc");fields.add(map);
map = new HashMap<String,String>();	map.put("value","discountPerc");map.put("label","Discount Perc");fields.add(map);
map = new HashMap<String,String>();	map.put("value","cost");map.put("label","Cost");fields.add(map);"""
ss=s.split('\n')

for i in range(0,len(ss)):
    psearch=re.compile(r'(?<=value",")\w+')
    p2search=re.compile(r'(?<=label",")\w+\s*?\w+')
    a1=re.findall(psearch,ss[i])[0]
    a2=re.findall(p2search,ss[i])[0]
    print('fields.put("%s","%s");'%(a1,a2))
