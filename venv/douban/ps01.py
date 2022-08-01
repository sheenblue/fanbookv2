import requests
from bs4 import BeautifulSoup
import dbtocsv
import re
from readxls import rowlist
from time import sleep

#url = "https://www.douban.com/search?cat=1001&q=%E5%B0%8F%E7%8E%8B%E5%AD%90"
def html(url):
  payload={

  }

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
  t = requests.get(url, headers=headers, data=payload)
  #print(t)
  t.encoding = 'utf-8'
  t = t.text

  soup = BeautifulSoup(t, 'lxml')
  return soup

def html2(url):
  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'bid=2mvywcyc6gg; douban-fav-remind=1; ll="118282"; __utmz=30149280.1657355541.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="146266157:hjFUBoZX1OE"; push_doumail_num=0; push_noty_num=0; __utmv=30149280.14626; gr_user_id=0501d6f8-1197-469d-80cb-afce6895bf77; _vwo_uuid_v2=D71F3B227871C344410B8C8993C614741|af51346524a36c151e591dc3cf80b606; ck=Rg1E; __utmc=30149280; __utmc=81379588; ap_v=0,6.0; __utma=30149280.474698133.1655008066.1659247139.1659250521.11; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=e78239c0-c9be-490a-b1fc-e3971c19da88; gr_cs1_e78239c0-c9be-490a-b1fc-e3971c19da88=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_e78239c0-c9be-490a-b1fc-e3971c19da88=true; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1659250526%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fcat%3D1001%26q%3D%25E4%25BC%258A%25E8%258E%258E%25E8%25B4%259D%25E6%258B%2589%25E4%25BC%25A0%22%5D; _pk_ses.100001.3ac3=*; __utma=81379588.2074708969.1659017092.1659247141.1659250526.7; __utmz=81379588.1659250526.7.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmt_douban=1; __utmb=30149280.21.10.1659250521; __utmt=1; __utmb=81379588.7.10.1659250526; _pk_id.100001.3ac3=801241b8d68b25e7.1659017092.7.1659251519.1659247141.',
    'Referer': 'https://search.douban.com/book/subject_search?search_text=%E6%AD%A5%E5%85%B5%E5%8F%B2%E8%AF%84%E8%AE%BA&cat=1001',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  #print(response)
  response.encoding = 'utf-8'
  response = response.text

  soup = BeautifulSoup(response, 'lxml')
  return soup


def vurl(t):
  #keyword = '三国演义'
  keyword = t
  url = requests.utils.quote(keyword) #转换编码
  url = f'https://www.douban.com/search?cat=1001&q={url}'
  #print(url)
  return url

#返回书本信息
def bookx(url,y):

  soup = html(url)  # 返回网页内容
  book = soup.find_all(class_='title') #获取所有书名
  for i in range(len(book)):
    bookname = book[i].find(name='a')
    if bookname.string == y:
      bookurl = str(bookname)
      reg1 = '2Fsubject%2F(.+?)%2'
      bookid = re.findall(reg1,bookurl)

      print('id',bookid)
      bookurl = f'https://book.douban.com/subject/{bookid[0]}/'
      # bookurl = bookurl['data-moreurl']
      # print('data-moreurl',bookurl)

      bookhtml = html2(bookurl)

      t = bookhtml.find(id='info')
      #t = t.find_all('span',class_='pl')
      #print(ts)

      alist = t.find_all(name='a')

      reg = '出版社|商务印书馆|上海三联书店|出版公司|中信出版集团|出版|衛城'
      authors = []
      publisher = []

      for i in range(len(alist)):
        #print(alist[i].string)
        if re.search(reg,alist[i].string):
          #print(alist[i].string)
          publisher.append(alist[i].string)
          break
        else:
          #print(alist[i].string)
          author = alist[i].string
          t1 = author.replace(' ', '')
          t1 = t1.replace('\n', '')

          authors.append(t1)

      print(authors)
      print(publisher)

      t1 = ''
      t2 = ''
      for i in range(len(authors)):
        t1 += authors[i]
      for i in range(len(publisher)):
        t2 += publisher[i]

      try:
        t3 = bookhtml.find(class_='intro')
        t3 = t3.find(name='p')
        t3 = t3.string
        print(t3)
      except:
        t3 = ''

      booklist = {"书名":t0,
             "作者":t1,
            "出版社":t2,
            "简介":t3}
      return booklist
    else:
      bookname = book[0].find(name='a')
      bookurl = str(bookname)
      reg1 = '2Fsubject%2F(.+?)%2'
      bookid = re.findall(reg1, bookurl)

      print('id', bookid)
      bookurl = f'https://book.douban.com/subject/{bookid[0]}/'
      # bookurl = bookurl['data-moreurl']
      # print('data-moreurl',bookurl)

      bookhtml = html2(bookurl)

      t = bookhtml.find(id='info')
      # t = t.find_all('span',class_='pl')
      # print(ts)

      alist = t.find_all(name='a')

      reg = '出版社|商务印书馆|上海三联书店|出版公司|中信出版集团|出版|衛城'
      authors = []
      publisher = []

      for i in range(len(alist)):
        # print(alist[i].string)
        if re.search(reg, alist[i].string):
          # print(alist[i].string)
          publisher.append(alist[i].string)
          break
        else:
          # print(alist[i].string)
          author = alist[i].string
          t1 = author.replace(' ', '')
          t1 = t1.replace('\n', '')

          authors.append(t1)

      print(authors)
      print(publisher)

      t1 = ''
      t2 = ''
      for i in range(len(authors)):
        t1 += authors[i]
      for i in range(len(publisher)):
        t2 += publisher[i]

      try:
        t3 = bookhtml.find(class_='intro')
        t3 = t3.find(name='p')
        t3 = t3.string
        print(t3)
      except:
        t3 = ''

      booklist = {"书名": t0,
                  "作者": t1,
                  "出版社": t2,
                  "简介": t3}
      return booklist


if __name__ == '__main__':
  try:
    name = input('请输入表格名字：')
    times = float(input('请输入休息时间：'))
    # name = '试炼'
    # times = 3
    bookname = rowlist(name)



    for i in range(len(bookname)):
      t0 = bookname[i][0]
      url = vurl(t0) #转换编码

      try:
        book1 = bookx(url,t0)

        dbtocsv.xieru(book1,t0)
      except Exception as e:
        print(e)
        print(f'【{t0}】==查无此书')

      sleep(times)
  except Exception as e:
    e = str(e)
    with open('err.txt','w+',encoding='utf-8')as f:
      f.write(e)


