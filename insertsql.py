#!/usr/bin/env python 2.7.5
#-*- coding:utf-8-*-
"""
插入wis_dataset_field脚本优化
"""
import re
file = open('e:/data1.txt')
lines=file.readlines()
file.close()
newfile=open('e:/data1new.txt','w')
p=r"""INSERT INTO wis_dataset_field   (SELECT  T1.VALUE_COLUMN ,T2.dataset_id),(.*?) (FROM IDGenerator_wms T1,wis_report_dataset T2 WHERE T1.PRIMARY_KEY_COLUMN='WisField_ID' AND T2.dataset_name='Shipping Label' AND T2.menu_id <>0)"""
p2=r"""INSERT INTO wis_dataset_field   (SELECT  T1.VALUE_COLUMN ,T2.dataset_id),(.*?) (FROM IDGenerator_wms T1,wis_report_dataset T2 WHERE T1.PRIMARY_KEY_COLUMN='WisField_ID' AND T2.dataset_name='Pick Ticket' AND T2.menu_id <>0)"""
pp=re.compile(p)
pp2=re.compile(p2)
field_id=40
id_count=0
count=0
count2=0
#field_id+count
pattern = re.compile(p)
for line in lines:
    if re.search(p,line):        
        id_count=id_count+1
        modified=pp.sub(r"""INSERT INTO wis_dataset_field values(%d,@datasetid+%d,\g<2>)"""% (field_id+id_count,count),line)
        count=count+1
        newfile.write(modified)
    elif re.search(p2,line):
        id_count=id_count+1
        modified=pp2.sub(r"""INSERT INTO wis_dataset_field values(%d,@datasetid2+%d,\g<2>)"""% (field_id+id_count,count2),line)
        count2=count2+1
        newfile.write(modified)
    else:
        newfile.write(line)
newfile.flush()
newfile.close()
