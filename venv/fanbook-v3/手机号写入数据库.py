#!/usr/bin/python3
#-*- coding = uft-8 -*-
# 创建数据库和表

import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('phones.db')

        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE employees(id integer PRIMARY KEY, phone INT)")

    con.commit()




if __name__ == '__main__':


    con = sql_connection()

    sql_table(con)