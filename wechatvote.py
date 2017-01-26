#! /usr/bin/env python3
# -*- coding : utf-8 -*-

'''
  An asistant tool for www.gxpx365.com
    Created by flty - 2016
'''


import string
import requests
import json
import time
import base64
import os
import re
import random

#Cookie: 1hfO_2132_saltkey=PYC7fRyY; 1hfO_2132_lastvisit=1485323160; __jsluid=50b7aa8da36bdc3cb1dd24713729f48b; hjbox_openid=oN8y8wUNggExbqcCfekwP6CaxxdE; safedog-flow-item=; 1hfO_2132_sid=Uddp9h; 1hfO_2132_lastact=1485334933%09plugin.php%09
'''
GET http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&model=ticket&zid=31&formhash=69a47e34&_=1485335604074 HTTP/1.1
Host: www.yangshuolife.com
Connection: keep-alive
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043024 Safari/537.36 MicroMessenger/6.3.32.960 NetType/WIFI Language/zh_CN
Referer: http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&model=votea&vid=1&from=timeline
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: 1hfO_2132_saltkey=PYC7fRyY; 1hfO_2132_lastvisit=1485323160; __jsluid=50b7aa8da36bdc3cb1dd24713729f48b; hjbox_openid=oN8y8wUNggExbqcCfekwP6CaxxdE; safedog-flow-item=; 1hfO_2132_sid=lrD8Aj; 1hfO_2132_lastact=1485335604%09plugin.php%09


'''
s = requests.session()

headers = {'Host': 'www.yangshuolife.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043024 Safari/537.36 MicroMessenger/6.3.32.960 NetType/WIFI Language/zh_CN',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/sharpp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,en-US;q=0.8'
}

s.headers = headers

# load_cookiejar = cookielib.LWPCookieJar()

# load_cookiejar.load('cookies.txt', ignore_discard=True, ignore_expires=True)

# load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)

# s.cookies = requests.utils.cookiejar_from_dict(load_cookies)

#https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx48092237f554528f&redirect_uri=http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&response_type=code&scope=snsapi_base&state=45

appid = 'wx48092237f554528f'

def genOpenID():
    charSeq = string.ascii_letters + string.digits
    randString = 'oN8y8w'
    for i in range(22):
        randString += random.choice(charSeq)
    return randString


def login(openid, zid):
    urlIndex = 'http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&model=detail&zid=%s&from=groupmessage&isappinstalled=0'%zid
    urlLogin = 'http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&code=%s&state=%s'%(openid, zid)
    urlGuanZu = 'http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&model=votea&vid=1'

    
    urlVote = 'http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&model=ticket'

    r = s.get(urlIndex, allow_redirects=False)

    print(r.headers['Location'])
    r = s.get(urlLogin)
    print(r.text)

    s.cookies['hjbox_openid'] = openid
    s.headers['Referer'] = r.url

    r = s.get(urlIndex)
    print(r.text)



    regexes = re.compile(r"formhash:'(.+)'")
    m = regexes.findall(r.text)
    formhash = m[0]
    s.headers['Referer'] = r.url
    urlClicks = 'http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&model=clicks&vid=1&zid=%s&formhash=%s'%(zid, formhash)
    r = s.get(urlClicks)
    print(r.text)


    # r = s.get(urlGuanZu)
    # print(r.text)
    # r = s.get(urlClicks)
    # print(r.text)

    timestamp = str(time.time())+'1'
    timestamp = timestamp.replace('.','')
    data = {'zid':zid, 'formhash':formhash, '_':timestamp}

    s.headers['Referer'] = r.url
    r = s.post(urlVote, data = data )
    print(r.text)
    r = s.get(urlClicks)
    print(r.text)



    # r = s.get(urlAction, verify=False)
    # print(r.text)
    return 0

def login1(openid, zid):
    urlIndex = 'http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&model=detail&zid=%s&from=groupmessage&isappinstalled=0'%zid
    r = s.get(urlIndex)

    print(r.headers['Location'])

    urlLogin = 'http://www.yangshuolife.com/plugin.php?id=hejin_toupiao&code=%s&state=%s'%(openid, zid)
    r = s.get(urlLogin)
    print(r.text)

if __name__ == '__main__':
    openid = genOpenID()
    print(openid)
    login1(openid, '2')

