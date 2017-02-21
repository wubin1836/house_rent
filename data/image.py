# -*- coding: utf-8 -*-    

import urllib,urllib2
import re
import os
import time

def getHtml(url):
    reg = r'<div class="thumbnail">(.+?</ul>)'
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    html = re.search(reg,html,re.S)
    return html


f = open('total7.csv','rb')
ff=f.read()
num= re.findall(r"zufang/(.+?)\.html",ff)
a=len(num)
print a
url1="http://bj.lianjia.com/zufang/"
for x in range(0,a):
    print num[x]
    url2=url1+num[x]+'.html'
    html = getHtml(str(url2))
    if html>0:
        html = html.group(0).decode('utf8')
    else:
        continue
    num2=num[x]
    reg1 = u'([\u4e00-\u9fa5]+)'
    reg2 = u'.*src="(.*)" alt=.*'
    labels = re.findall(reg1,html)
    imgurls = re.findall(reg2,html)
    b=len(imgurls)
    if labels>0:
        for y in range(0,b):
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent' : user_agent }
            req = urllib2.Request(imgurls[y],headers = headers)
            try:
                imghtml = urllib2.urlopen(req,timeout = 10)
            except Exception, e:
                print 'Exception:' + str(e)
                continue
            try:
                img = open("I:/pic3/" + labels[y] + '_'+'%s.jpg' % num2, 'w+b')
                img.write(imghtml.read())
                img.close()
            except Exception, e:
                print 'Exception:' + str(e)
                continue
            
    else:
        continue
  
f.close()
