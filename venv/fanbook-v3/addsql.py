#!/usr/bin/python3
#-*- coding = uft-8 -*-
# 插入数据

import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('phones.db')

        return con

    except Error:

        print(Error)

def sql_insert(con, entities):
    cursorObj = con.cursor()

    cursorObj.execute(
        'INSERT INTO employees(phone) VALUES(?)', entities)

    con.commit()
def sql_fetch(con,query,phonenum):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT *  FROM employees WHERE phone = ?',query)

    rows = cursorObj.fetchall()

    if rows == []:
        print('手机号未注册了')
        entities = (phonenum,)
        sql_insert(con, entities)
        con.commit()
        print('手机号插入成功')
        con = sqlite3.connect('phones.db')

        # program statements

        con.close()
        return 1
    else:
        print('手机号已注册')
        return 0









if __name__ == '__main__':
    con = sql_connection()
    phonenum = 1581659322
    query = (phonenum,)  #删除的数据是元组类型，因此1后面应该有逗号，修改后cur.execute(sql,(1,)，可以成功执行；
    t = sql_fetch(con,query,phonenum)
    if t == False:
        print(t)
