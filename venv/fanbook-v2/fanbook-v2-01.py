#!/usr/bin/python3
#-*- coding = uft-8 -*-

from os import getcwd
from os.path import join
from pyautogui import dragTo,click,hotkey,moveTo,typewrite,size,locateCenterOnScreen,FAILSAFE,PAUSE
from time import sleep
from re import findall
import pyperclip
import requests
from random import choice
from json import loads
import newphone
import readxls

#1 单击坐标
def oneclick(t):
    moveTo(t)
    click()
    sleep(0.4)


#2 时间延迟
def sleeptime(t):
    t = str(int(t))
    sleep(t)
#3 复制
def copyvalue(t):
    t = eval(t)
    pyperclip.copy(t)
    sleep(0.4)


#4 执行快捷键
def runhotkey(t):
    hotkey(t)

#5 识别图片并单击
def picclick(t):
    t = str(int(t))
    t = f'./pic/{t}.png'
    i = 1
    wait = 0
    while i == 1:
        coords = locateCenterOnScreen(t)  # 返回image屏幕上中心的（x，y）坐标
        if coords == None:

            if wait == 20:
                print('跳出')
                break
            else:
                print('没找到内容')
                # sleep(1)
                wait += 1
                i = 1
        else:
            click(coords)
            i = 2
    sleep(0.4)

#6 赋值
def fuvalue(t):
    t = eval(t)

#7 模拟手动输入
def autowrite(t):
    t = eval(t)
    typewrite(t, interval=0.25)

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
def yam(phone):
    num_code = newphone.Newyzm(phone)
    while 1:
        if num_code != '尚未收到包含关键字“fanbook”的短信，请5秒后再收取。请确保设置了正确的关键字。[尚未收到]':
            num_code = newphone.reyzm(num_code)
            return num_code
        else:

            num_code = newphone.Newyzm(phone)
            print('重新获取验证码')
            min += 1
            print(f'已进行了{min}秒')
            if min == 120:
                hotkey('Ctrl', 'w')
                break
            else:
                pass


#10 判断是否已加入服务器
def addserve1(t,y):
    t = str(int(t))
    t = f'./pic/{t}.png'
    if t != None:
        print("进入1线")
        main(y)
    else:
        print('不是1线')
        pass


#11 判断是否未加入服务器
def addserve2(t,y):
    t = str(int(t))
    t = f'./pic/{t}.png'
    if t != None:
        print("进入1线")
        main(y)

    else:
        pass

#12 判断是否有点击邀请码
def addserve3(t,y):
    t = str(int(t))
    t = f'./pic/{t}.png'
    if t != None:
        print("进入3线")
        main(y)

    else:
        pass


#13 判断是否需要设置头像
def addserve4(t,y):
    t = str(int(t))
    t = f'./pic/{t}.png'
    if t != None:
        print("进入4线")
        main(y)

    else:
        pass

#14 拖拽
def drags(t):
    dragTo(t, duration=0.5)

#15 判断有没有立即开始
def addserve4(t,x,y):
    t = str(int(t))
    t = f'./pic/{t}.png'
    if t != None:
        print("进入4线")
        main(x)

    else:
        main(y)
        pass

def onestep(t):



if __name__ == '__main__':
    t = readxls.sheets(1)
    print(t)