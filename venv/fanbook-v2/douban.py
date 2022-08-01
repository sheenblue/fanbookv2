# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-07-27
# @FILE   : douban.py

import requests
from bs4 import BeautifulSoup
import os
import time
import json



payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'bid=7i02YJWSMk8; douban-fav-remind=1; __gads=ID=160d730e9fe14487-22b8ee42b1d3004e:T=1657704934:RT=1657704934:S=ALNI_MYn_2sBwTl3KbzZy0bLZSAEOdETFA; __gpi=UID=000007ab822c482a:T=1657704934:RT=1657704934:S=ALNI_MaANsHTUZALqfMgdMzlRCzRA65hCQ; ll="118282"; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=D57C62205BC2EB2FCF7F1A82750879E77|17ca1a683c24e17de0b2bfa0df4e3728; ap_v=0,6.0; dbcl2="146266157:hjFUBoZX1OE"; ck=Rg1E; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1658899959%2C%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%5D; _pk_id.100001.4cf6=7fb089fc8a04738b.1658806672.3.1658899959.1658897853.; _pk_ses.100001.4cf6=*; __utma=30149280.1060122967.1657704959.1658897813.1658899959.4; __utmb=30149280.0.10.1658899959; __utmz=30149280.1658899959.4.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1793085960.1658806672.1658897813.1658899959.3; __utmb=223695111.0.10.1658899959; __utmz=223695111.1658899959.3.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
  'Referer': 'https://open.weixin.qq.com/',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}



user_list = []
dict()
for y in range(0,550,20):

    url = f"https://movie.douban.com/subject/35168646/comments?start={y}&limit=20&status=P&sort=new_score"
    response = requests.request("GET", url, headers=headers, data=payload)
    html_str = response.text

    bs = BeautifulSoup(html_str, 'lxml')



    avaurl = bs.find_all('div',class_='avatar') #获取元素的上级
    #print(avaurl)

    for i in range(len(avaurl)):
        names = avaurl[i].find_all('a')  # 获取所有用户名的的内容
        imgs = avaurl[i].find_all('img')  # 获取所有头像链接

        name = names[0]['title'] #提取单个用户名

        if len(name) == 1:
            name = f'{name}haha'
            print('----------------------------修改后的名字:',name)
        else:
            print(name)
            pass


        url = imgs[0]['src'] #提取单个头像链接
        print(url)

        user_list.append(dict(  #把数据放入字典
            name = name,
            url = url
        ))
        time.sleep(0.3)

#print(user_list)
userjson = json.dumps(user_list,indent=4,ensure_ascii=False)
#print(userjson)
with open('userjson9.json','w',encoding='utf-8') as f:
    f.write(userjson)
