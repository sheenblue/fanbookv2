#!/usr/bin/python3
#-*- coding = uft-8 -*-
import time
import logging
import requests
from re import findall
import addsql
import sqlite3

def rephone(t):
    t = str(t)

    patt = "b'(.+?)'"
    title = findall(patt, t)
    print(title[0])
    return title[0]


# 正则排出验证码
def reyzm(t):
    t = str(t)
    patt = "验证码：(.+?)（5分钟内有效"
    title = findall(patt, t)
    print(title[0])
    return title[0]


# 生成新手机号
def Newphone():
    token = 'd8a1fe5360344e839d23772e44984227'
    while 1:
        phone = requests.get(f'http://api.d1jiema.com/zc/data.php?code=getPhone&token={token}')
        print(phone.status_code)

        if phone.status_code == 200:
            #print(phone.content)
            phone = phone.content
            phone = rephone(phone)
            return phone




# 提取验证码
def Newyzm(phone):
    token = 'd8a1fe5360344e839d23772e44984227'
    while 1:
        dx = requests.get(f'http://api.d1jiema.com/zc/data.php?code=getMsg&token={token}&phone={phone}&keyWord=fanbook')
        dx.encoding = 'utf-8'
        if dx.status_code == 200:
            # print(dx.content)
            dx = dx.text
            print(dx)
            return dx




if __name__ == '__main__':
    phone = Newphone() #生成一个新手机号
    #写入数据库
    con = addsql.sql_connection()
    phonenum = int(phone)
    query = (phonenum,)  # 删除的数据是元组类型，因此1后面应该有逗号，修改后cur.execute(sql,(1,)，可以成功执行；
    t = addsql.sql_fetch(con, query, phonenum)
    if t == False:
        print(t)


    time.sleep(30)
    num_code = Newyzm(phone)
    while 1:
        if num_code != '尚未收到包含关键字“fanbook”的短信，请5秒后再收取。请确保设置了正确的关键字。[尚未收到]':
            newyzm = reyzm(num_code)
            break
        else:

            num_code = Newyzm(phone)
            print('重新获取验证码')
            min += 1
            print(f'已进行了{min}秒')
            if min == 120:
                break
            else:
                pass

