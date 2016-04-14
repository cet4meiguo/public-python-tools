#!/usr/bin/python 2.7
#-*- coding:utf-8 -*-
def p2s(jpql):
    """
    jpql to sql
    """
    sql=''
    before = ''
    for i in jpql:
        if i.isupper():
            if before==' ':
                sql+=str(i).lower()
            else:
                sql +='_'+i.lower()
	else:
            sql+=str(i)
        before = i
    return sql
