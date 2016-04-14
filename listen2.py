#!/usr/bin/env python
#-*- coding:utf-8 -*-

import weibo
import json
import os
import sys
import time
#import mailimages
import urllib
"""
获取uid 最新发表的微博列表(只能是自己的uid:微博id)
接口:
statuses/user_timeline
调用方式:
client.statuses.user_timeline.get(uid=自己的uid)
"""
uid='xx'#更换自己的uid
def eachCall(client,maxId):
    """
    获取自己关注列表发布的微博信息
    """
    if maxId==0:
        callback = client.statuses.friends_timeline.get(count=100)#每次运行,第一次获得100条微博记录.100为最大值
    else:
        callback = client.statuses.friends_timeline.get(count=10)#之后每次获得10条记录,可随意修改,100为最大值
    newMaxId = callback.statuses[0].id
    
    for status in callback.statuses:
        id = status.id
        if id<=maxId:
            break;
        create_at = status.created_at
        user = status.user.name
        text = status.text
        
        pic_urls = status.pic_urls
        if 'retweeted_status' in status.keys():
            retweeted_status = status.retweeted_status
            retweeted_info = getNameText(retweeted_status,id)
            mailContent = text+'['+retweeted_info[0]+':'+retweeted_info[1]+']'
        else:
            mailContent = text
        #"""
        content = user+"\t"+create_at+"\t"+str(id)+"\n\t"+mailContent+"\n"
        print(content)
        
    return newMaxId
def run(client,maxId=0):
    #server = mailimages.login()
    maxId = eachCall(client,maxId)

def comment(client,id,comment):
    client.comments.create.post(id=id,comment=comment)
love=u"""关关雎鸠在河之洲窈窕淑女君子好逑参差荇菜左右流之窈窕淑女寤寐求之求之不得寤寐思服悠哉悠哉辗转反侧参差荇菜左右采之窈窕淑女琴瑟友之参差荇菜左右芼之窈窕淑女钟鼓乐之"""
print(len(love))
#s=love.encode('gbk')
def comments(client,id):
    for i in range(0,len(love)/4):
	print(time.strftime("%Y-%m-%d %H:%M:%S"))
        comment(client,id,love[(4*i):(4*i+4)])
        time.sleep(60)

 
