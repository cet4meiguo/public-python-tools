
import re
import urllib

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getimg(html):
    reg=r'src="(.*?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)
        print x
        x+=1

html=getHtml("http://tieba.baidu.com/p/2460150866?see_lz=1")
getimg(html)
