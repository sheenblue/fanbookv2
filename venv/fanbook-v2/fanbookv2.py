#!/usr/bin/python3
#-*- coding = uft-8 -*-

from os import getcwd
from os.path import join
from pyautogui import dragTo,click,hotkey,moveTo,typewrite,size,locateCenterOnScreen,alert
from time import sleep
from re import findall
import pyperclip
import requests
from random import choice
from json import loads
import newphone
import readxls
import txname
import onetogo
import addsql

#1 单击坐标
def oneclick(t):
    t = str(t)
    t = t.split(',')
    x, y = int(t[0]), int(t[1])
    moveTo(x,y)
    click()
    sleep(0.4)


#2 时间延迟
def sleeptime(t):
    t = int(t)
    sleep(t)
#3 复制
def copyvalue(t):
    t = eval(t)
    pyperclip.copy(t)
    print(t)
    sleep(0.4)


#4 执行快捷键
def runhotkey(t):
    t = t.split(',')
    if len(t) == 3:
        x,y,z = t[0],t[1],t[2]
        print(x,y,z)
        hotkey(x,y,z)
    elif len(t) == 2:
        x, y = t[0],t[1]
        print(x, y)
        hotkey(x, y)
    elif len(t) == 1:
        x = t[0]
        print(x)
        hotkey(x)

    sleep(0.4)

#5 识别图片并单击
def picclick(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    print(t)
    i = 0
    wait = 0
    while 1:
        print('start ocr')
        coords = locateCenterOnScreen(t)  # 返回image屏幕上中心的（x，y）坐标
        print(coords)
        if coords == None:

            if wait == 20:
                print('跳出')
                return True
            else:
                print('没找到内容')
                # sleep(1)
                wait += 1
                i = 1
        else:
            click(coords)
            print('点击成功')

            return False
    sleep(0.4)

#6 赋值
def fuvalue(t):
    t = eval(t)

#7 模拟手动输入
def autowrite(t):
    t = eval(t)
    typewrite(t, interval=0.25)
    sleep(0.4)

#8 判断图片是否还在
def imgcz(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    xy = locateCenterOnScreen(t)
    if xy != None:  # 如果头像设置未成功
        print('头像设置未成功')
        hotkey('Ctrl','w')
        # moveclick(1897, 19)
        return 0
    else:
        print('头像设置成功')
        return 1
#9  收取验证码
def yam(t):
    t = eval(t)
    print('手机号',t)
    global num_code
    num_code = newphone.Newyzm(t)
    min = 0
    while 1:
        if num_code != '尚未收到包含关键字“fanbook”的短信，请5秒后再收取。请确保设置了正确的关键字。[尚未收到]':
            num_code = newphone.reyzm(num_code)
            return num_code
        else:

            num_code = newphone.Newyzm(t)
            print('重新获取验证码')
            min += 1
            print(f'已进行了{min}秒')
            if min == 120:
                print('退出注册')
                hotkey('Ctrl','w')
                return False
            else:
                pass


#10 判断是否已加入服务器
def addserve1(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    t = locateCenterOnScreen(t)
    print('1线',t)
    if t != None:
        print("=======================进入1线")
        onestep(action5)
        return True

    else:
        print('=======================不是1线')

        return False

#11 判断是否未加入服务器
def addserve2(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    t = locateCenterOnScreen(t)
    if t != None:
        print("=======================进入2线")
        onestep(action4)
        return True

    else:
        sleep(0.4)
        pass

#12 判断是否有点击邀请码
def addserve3(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    t = locateCenterOnScreen(t)
    if t != None:
        print("=======================进入3线")
        onestep(action3)
        return True

    else:
        sleep(0.4)
        pass


#13 判断是否需要设置头像
def addserve4(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    t = locateCenterOnScreen(t)
    if t != None:
        print("=======================进入4线")
        onestep(action2)
        onestep(action3)
        return True

    else:

        sleep(0.4)

        pass

#14 拖拽
def drags(t):
    t = str(t)
    t = t.split(',')
    x, y = int(t[0]), int(t[1])
    dragTo(x,y, duration=0.5)

#15 判断有没有立即开始
def addserve5(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    t = locateCenterOnScreen(t)
    if t != None:
        print("=======================进入501线")
        onestep(action7)
        return True

    else:
        print("=======================进入502线")
        #关闭浏览器
        onestep(action6)
        return True

        pass

#16 加添手机号码到库里
def addphone(t):
    t = eval(t)
    addsql.sql_insert(con,t)



def onestep(t):

    for i in range(len(t)):
        print(t[i])
        if t[i][0] == 1.0:
            oneclick(t[i][2])
        elif t[i][0] == 2.0:
            sleep(t[i][2])
        elif t[i][0] == 3.0:
            copyvalue(t[i][2])
        elif t[i][0] == 4.0:
            runhotkey(t[i][2])
        elif t[i][0] == 5.0:
            picclick(t[i][2])
        elif t[i][0] == 6.0:
            fuvalue(t[i][2])
        elif t[i][0] == 7.0:
            autowrite(t[i][2])
        elif t[i][0] == 8.0:
            imgcz(t[i][2])
        elif t[i][0] == 9.0:
            reuslt0 = yam(t[i][2])
            if reuslt0 == False:
                print(t[i])
                print('over')
                break
        elif t[i][0] == 10.0:
            reuslt1 = addserve1(t[i][2])
            if reuslt1 == True:
                print(t[i])
                print('over')
                break
        elif t[i][0] == 11.0:
            reuslt2 = addserve2(t[i][2])
            if reuslt2 == True:
                print(t[i])
                print('over')
                break
        elif t[i][0] == 12.0:
            reuslt3 = addserve3(t[i][2])
            if reuslt3 == True:
                print(t[i])
                print('over')
                break
        elif t[i][0] == 13.0:
            reuslt4 = addserve4(t[i][2])
            if reuslt4 == True:
                print(t[i])
                print('over')
                break
        elif t[i][0] == 14.0:
            drags(t[i][2])
        elif t[i][0] == 15.0:
            addserve5(t[i][2])
        elif t[i][0] == 16.0:
            addphone(t[i][2])
        else:
            print('程序有误')
            break





if __name__ == '__main__':
    try:
        sleep(3)
        global phone
        global num_code
        url = 'https://fanbook.mobi/web/login'
        yqmz = 'LKi7KFLN'
        #print('第一次生成的手机号：', phone)
        num_code = 111111
        nft = 'nft'
        content = '窗画廊万岁！'


        action1 = readxls.sheets(0)
        action2 = readxls.sheets(1)
        action3 = readxls.sheets(2)
        action4 = readxls.sheets(3)
        action5 = readxls.sheets(4)
        action6 = readxls.sheets(5)
        action7 = readxls.sheets(6)
        print('请输入要注册的次数：')
        zhuce = int(input('注册次数：'))
        for i in range(zhuce):

            phone = newphone.Newphone()  # 生成一个新手机号
            #phone = '15816765263'
            print('=========================',phone)
            # 生成头像和名字
            tname = txname.main()  # 获取一个名字列表
            fname = txname.txname2(tname)  # 随机取一个名字
            txpath = txname.imgfile(fname)  # 用上面的名字生成图片地址
            #phone = fanbookv2.phone

            # 写入数据库
            con = addsql.sql_connection()
            #phone = int(phone)
            t = addsql.sql_fetch(con,phone)

            if t == False:

                print(t)
                print('终止程序')

            else:
                print('开始注册')

                # 生成六个动作组

                onestep(action1)
                # break
        alert(text='程序已结束',title='17',button='OK')
    except Exception as e:
        with open('err.txt','a')as f:
            f.write(e)