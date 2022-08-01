# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-07-27
# @FILE   : dltx.py

import requests
import json
url = "https://movie.douban.com/subject/35231822/comments?status=P"

payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'bid=S31qgTPvJoo; gr_user_id=372f7e2d-1774-4b92-ade3-37e448fb53da; viewed="2814111_11500082"; ll="118282"; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=D1E8916F2E1983FE444B27FA02C6ABECC|3d37a613bcc3b3d14e0df195bc66ba83; _ga=GA1.2.1744812078.1653540178; _gid=GA1.2.134697879.1657002648; __utmz=30149280.1657003455.16.12.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utma=30149280.1744812078.1653540178.1657003455.1657072218.17; __utmb=30149280.1.10.1657072218; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1657072791%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.21071204.1654149975.1657003455.1657072791.9; __utmb=223695111.0.10.1657072791; __utmz=223695111.1657072791.9.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=49f6c63bf759e9b3.1654149975.10.1657073350.1657003462.',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.103.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="99", "_Not(A:Brand";v="8", "Chromium";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

#response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

with open('userjson9.json','r',encoding='utf-8') as f:
   t = f.read()
   dicts = json.loads(t)

for i in range(len(dicts)):
  name = dicts[i]['name']
  url = dicts[i]['url']
  img = requests.get(url, headers=headers, data=payload)
  img = img.content
  img_name = f'./tx/{name}.jpg'
  with open(img_name,'wb') as f:
    f.write(img)
  print(f'{name} download succeed')
#print(len(dicts))