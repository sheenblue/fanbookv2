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
        'INSERT INTO employees(id, phone) VALUES(?, ?)', entities)

    con.commit()




if __name__ == '__main__':
    con = sql_connection()
    entities = (2, 13592872495)

    sql_insert(con, entities)