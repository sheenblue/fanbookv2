import requests
from bs4 import BeautifulSoup
import dbtocsv
import re
from readxls import rowlist
from time import sleep

url = 'https://www.douban.com/search?cat=1001&q=%E8%AE%BA%E6%8C%81%E4%B9%85%E6%88%98'
payload={}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'bid=2mvywcyc6gg; douban-fav-remind=1; ll="118282"; __utmz=30149280.1657355541.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="146266157:hjFUBoZX1OE"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14626; ck=Rg1E; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1659016131%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DqSJAiuhZP1_BP4NtNdihtSbLPyPi_e9q0XS3rzylutjeX4--xZVBVFsG1WxlvZ73%26wd%3D%26eqid%3Da82551f20000f9240000000662c93d13%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.474698133.1655008066.1657355541.1659016131.5; __utmc=30149280; __utmt=1; _pk_id.100001.8cb4=f55fcb4c66f39c62.1655008064.6.1659016277.1657355542.; __utmb=30149280.8.10.1659016131',
    'Referer': 'https://www.douban.com/search?source=suggest&q=%E5%B0%8F%E7%8E%8B%E5%AD%90',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response)

response.encoding = 'utf-8'
response = response.text

soup = BeautifulSoup(response, 'lxml')
#soup = html(url)  # 返回网页内容
book = soup.find_all(class_='title')

for i in range(len(book)):
  bookname = book[i].find(name='a')
  print(bookname.string)
#bookurl = book.find(name='a')