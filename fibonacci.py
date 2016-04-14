#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-

"""
fibonacci
"""
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
