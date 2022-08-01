#!/usr/bin/python3
#-*- coding = uft-8 -*-



from os import getcwd
from os.path import join
from pyautogui import dragTo,click,hotkey,moveTo,typewrite,size,locateCenterOnScreen,FAILSAFE,PAUSE
from time import sleep
from re import findall
import pyperclip
#from pyperclip import pyperclip.copy
import requests
from random import choice
from json import loads

try:

    #pyautogui.FAILSAFE =False
    #pyautogui.PAUSE = 0.5
    def onClick(pngfile):

        i = 1
        wait = 0
        # print(type(coords))
        while i == 1:
            coords = locateCenterOnScreen(pngfile)  # 返回image屏幕上中心的（x，y）坐标
            if coords == None:
                #print('没找到内容')
                # if wait == 100:
                #     print('跳出')
                #     break
                # else:
                #     print('没找到内容')
                    sleep(1)
                    wait += 1
                    i = 1
            else:
                click(coords)
                print('点击成功')
                i = 2

        #右击该坐标点
        return coords

    #判断有没有加入服务器
    def yz(p):
        coords = locateCenterOnScreen(p)  # 返回image屏幕上中心的（x，y）坐标
        return coords
    #正则排出手机号
    def rephone(t):
        t = str(t)

        patt = "b'(.+?)'"
        title = findall(patt, t)
        print(title[0])
        return title[0]
    #正则排出验证码
    def reyzm(t):
        t = str(t)
        patt = "验证码：(.+?)（5分钟内有效"
        title = findall(patt, t)
        print(title[0])
        return title[0]
    #生成新手机号
    def Newphone():
        token = 'd8a1fe5360344e839d23772e44984227'
        phone = requests.get(f'http://api.d1jiema.com/zc/data.php?code=getPhone&token={token}')
        print(phone.content)
        phone = phone.content
        phone = rephone(phone)

        return phone
    #提取验证码
    def Newyzm(phone):
        token = 'd8a1fe5360344e839d23772e44984227'
        dx = requests.get(f'http://api.d1jiema.com/zc/data.php?code=getMsg&token={token}&phone={phone}&keyWord=fanbook')
        dx.encoding = 'utf-8'
        # print(dx.content)
        dx = dx.text
        print(dx)
        return dx

    #随机取名和头像
    def txname2():



        name4 = choice(dicts)
        txname1 = name4['name']
        return  txname1
    def imgfile(t):
        pwd = getcwd()
        txfile = f'{t}.jpg'

        txfile = join(pwd, 'tx','3', txfile)
        return txfile

    def AddServe2():
        #sleep(1)
        ts(ltimes[23])
        #等待点击服务器头像
        #点击服务器头像
        imgzh(shotlist[4])
        #等待点击加入服务器
        #sleep(2)
        ts(ltimes[24])
        #判断有没有加入过
        started = yz(shotlist[14][1])
        # 如果有直接退出
        if started == None:
            print('加入过，直接退出')
            imgzh(shotlist[5])
            #sleep(2)
            ts(ltimes[12])
            # 点击退出登录
            # onClick(out)
            imgzh(shotlist[6])
            # 点击确定
            #sleep(1)
            ts(ltimes[11])
            print(xylist[9])
            mc(xylist[9])
            #sleep(1)
            ts(ltimes[11])
            mc(xylist[10])
        else:

            # 点击立即开始
            #onClick(start)

            imgzh(shotlist[14])
            sleep(1)
            # 点击同意规则
            print('同意')
            imgzh(shotlist[15])
            # onClick(agree)
            # 下拉
            x2, y2 = mc2(xylist[3])
            dragTo(x2, y2, duration=0.5)
            imgzh(shotlist[19])
            sleep(1)

            #imgzh(shotlist[20])
            mc(xylist[8])
            mc(xylist[7])
            #moveclick(1160,234)
           # moveclick(1111, 732)

            #发送内容
            #onClick(send)
            imgzh(shotlist[21])
            content = '窗画廊万岁！'
            pyperclip.copy(content)
            sleep(1)
            hotkey('Ctrl', 'v')
            hotkey('enter')
            sleep(1)
            # 点击设置
            # onClick(setup)
            imgzh(shotlist[5])
            sleep(2)
            # 点击退出登录
            # onClick(out)
            imgzh(shotlist[6])
            # 点击确定
            sleep(1)
            print(xylist[9])
            mc(xylist[9])
            sleep(1)
            mc(xylist[10])

    def AddServe3():
        # 点击添加

        #onClick(addpic)
        imgzh(shotlist[22])
        # 加入服务器79923
        #onClick(addserves)
        imgzh(shotlist[23])
        adds()
    def adds():
        # 输入邀请码
        imgzh(shotlist[12])
        # onClick(yqm)
        yqmz = 'LKi7KFLN'
        pyperclip.copy(yqmz)
        hotkey('Ctrl', 'v')
        # 点击加入服务器
        # onClick(addserve)
        imgzh(shotlist[13])
        # 点击接受邀请
        # onClick(jsyq)
        #等待点击邀请
        #sleep(3)
        ts(ltimes[22])
        print('点击接受邀请')
        mc(xylist[2])
        # moveclick(953,711)
        print('准备点击立即开始')
        #等待点击开始
        #sleep(3)
        ts(ltimes[21])
        # 点击立即开始
        # onClick(start)
        imgzh(shotlist[14])
        #等待点击同意
        #sleep(1)
        ts(ltimes[20])
        # 点击同意规则
        print('同意')
        imgzh(shotlist[15])
        # onClick(agree)
        # 下拉
        x2, y2 = mc2(xylist[3])
        dragTo(x2, y2, duration=0.5)
        # dragTo(1007, 715, duration=0.5)
        # sleep(3)
        # 点击下一步
        # onClick(agree)nft
        # moveclick(1106,906)
        imgzh(shotlist[16])
        #等待输入昵称
        #sleep(1)
        ts(ltimes[19])

        # 输入昵称
        # onClick(name)
        # moveclick(937,657)
        #imgzh(shotlist[17])
        mc(xylist[5])
        txname = fanbook_name
        pyperclip.copy(txname)
        hotkey('Ctrl', 'v')
        #等待输入NFT
        ts(ltimes[18])
        #sleep(2)
        # 输入NFT
        # moveclick(950,742)
        #imgzh(shotlist[18])

        mc(xylist[6])
        # onClick(nft)
        # sleep(1)
        nft2 = 'nft'
        pyperclip.copy(nft2)
        hotkey('Ctrl', 'v')
        #等待点击完成
        #sleep(1)
        ts(ltimes[16])
        # 点击完成
        #onClick(finish2)
        imgzh(shotlist[19])
        #等待点击弹窗
        #sleep(0.5)
        ts(ltimes[17])

        mc(xylist[7])
        # moveclick(1111,732)
        #等待点击关闭
        ts(ltimes[15])
        #sleep(2)
        # 点击关闭
        mc(xylist[8])
        #imgzh(shotlist[20])
        mc(xylist[7])
        # moveclick(1160,234)
        # moveclick(1111, 732)

        # 发送内容
        # onClick(send)
        imgzh(shotlist[21])
        content = '窗画廊万岁！'
        print('content',content)
        #等待复制内容
        ts(ltimes[14])
        #sleep(1)
        pyperclip.copy(content)
        hotkey('Ctrl', 'v')
        hotkey('enter')
        #等待点击设置
        ts(ltimes[13])
        #sleep(1)
        # 点击设置
        # onClick(setup)
        imgzh(shotlist[5])
        #等待点击退出
        ts(ltimes[12])
        #sleep(2)
        # 点击退出登录
        # onClick(out)
        imgzh(shotlist[6])
        # 点击确定
        ts(ltimes[11])
        #sleep(1)
        mc(xylist[9])
        #sleep(1)
        # mc(xylist[10])
        # moveclick(1063,604)

    def AddServe4():
        # 点击我有邀请码
        #onClick(cyqm)
        #mc(xylist[23])
        imgzh(shotlist[11])
        #等待输入邀请码
        ts(ltimes[10])
        #sleep(2)
        # 输入邀请码
        adds()
    #click
    def moveclick(t,y):
        moveTo(t,y)
        click()
    #注册账号
    def qx():
        # 获取手机号
        phone = Newphone()

        print('准备输入手机号')


        imgzh(shotlist[0])

        print('输入手机号')


        #onClick(cphone)

        typewrite(phone, interval=0.25)
        # 勾选公约
        imgzh(shotlist[1])
        #onClick(conventions)
        # 勾选自动登录
        #onClick(Login)
        #imgzh(shotlist[2])
        #sleep(3)

        # 获取验证码
        print(shotlist[3])
        imgzh(shotlist[3])
        #onClick(shotlist[3][1])
        #mc(xylist[15])

        # 输入验证码
        num_code = Newyzm(phone)
        min = 0
        newyzm = ''
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
        if min == 120:


            return 0
        else:

            sleep(1)
            newyzm = newyzm
            pyperclip.copy(newyzm)
            hotkey('Ctrl', 'v')
            return 1

        # onClick(code)
    #设置头像昵称
    def zc():

        #print(666)
        ts(ltimes[9])
        #sleep(1)
        print('进入注册模式')
        # 点击设置头像
        imgzh(shotlist[7])
        #onClick(Avatar)
        print('开始设置头像')
        # 激活输入框
        ts(ltimes[8])
        #sleep(3)
        #moveclick(484, 660)

        # onClick(Avatar_url)
        tx = touxiang
        print(tx)
        pyperclip.copy(tx)
        hotkey('Ctrl', 'v')
        # 获取头像链接 https://img1.doubanio.com/icon/u56822400-97.jpg
        #等待点击打开
        ts(ltimes[7])
        #sleep(2)
        print('点击打开')
        # 点击打开
        mc(xylist[0])
        #moveclick(791,501)
        # onClick(open)
        #判断头像设置成功否
        ts(ltimes[6])
        #sleep(2)
        #判断头像设置成功否
        ava2 = yz(shotlist[7][1])
        if ava2 != None:  #如果头像设置未成功
           print('头像设置未成功')
           mc(xylist[10])
           #moveclick(1897, 19)
           return 0
        else:
           print('头像设置成功')
           return 1




    #输入昵称
    def txhj():
        print('输入用户名')
        #等待输入昵称
        #sleep(1)
        ts(ltimes[5])
        # 输入昵称 抹香苏
        imgzh(shotlist[8])
        #moveclick(859,621)
        #onClick(user_name)

        txname = fanbook_name
        pyperclip.copy(txname)
        hotkey('Ctrl', 'v')
        # 选择性别
        #onClick(user_sex)
        imgzh(shotlist[9])
        #等待点击注册完成
        ts(ltimes[4])
        #sleep(0.5)

        # 点击完成
        imgzh(shotlist[10])
        #onClick(finish)
        #注册完毕等待加入服务器
        ts(ltimes[3])
        #sleep(2)
        print("加入服务器流程")
    #判断是否加入服务器
    def server():

        #print(123)
        #判断是否加入服务器时间等待
        #sleep(4)
        ts(ltimes[2])
        host2 = yz(shotlist[4][1])  # 已经加入服务器

        if host2 != None:
            print("进入2线")
            AddServe2()
        else:
            print('不是2线')
            pass

        host3= yz(shotlist[24][1]) #未加入服务器
        if host3 != None:
            print("进入3线")
            AddServe3()
            mc(xylist[10])
        else:
            pass

        host4= yz(shotlist[11][1])
        if host4 != None:
            print("进入4线")
            AddServe4()
            mc(xylist[10])
            #moveclick(1904, 19)
        else:
            pass
        host5 = yz(shotlist[7][1])
        if host5 != None:
            print("进入5线")
            txsz = zc()
            if txsz == 1:

                txhj()
                AddServe4()
                mc(xylist[10])
                #moveclick(1904, 19)
            else:
                sleep(3)
                #mc(xylist[10])
                pass
        else:
            pass
    #打开chrome
    def openchrome():
        moveclick(1, 1)
        ts(ltimes[1])
        pyperclip.copy('https://fanbook.mobi/web/login')
        #hotkey("winleft", "left")
        #moveclick(1, 1)
        hotkey('Ctrl', 'shift', 'n')
        ts(ltimes[1])
        pyperclip.copy('https://fanbook.mobi/web/login')
        pyperclip.copy('https://fanbook.mobi/web/login')
        #输入网址时间等待
        #sleep(0.5)
        ts(ltimes[1])
        hotkey('Ctrl', 'v')
        #ts(ltimes[1])
        hotkey('enter')

    def main():
        pdyzm = qx()
        if pdyzm == True:
            server()
        else:
            mc(xylist[10])
            #moveclick(1904, 19)
            pass
        # zc()
        # txhj()

    #输入坐标组转化成坐标
    def mc(z):
        #x, y = float(int(z[0]) * 1 / 2 * x1), float(int(z[1]) * 1 / 2 * y1)
        x, y = float(int(z[0])  * x1), float(int(z[1])  * y1)
        #print(x,y)
        moveclick(x,y)

        return x,y
    def mc2(z):
        #x, y = float(int(z[0]) * 1 / 2 * x1), float(int(z[1]) * 1 / 2 * y1)
        x, y = float(int(z[0])  * x1), float(int(z[1])  * y1)
        #print(x,y)


        return x,y

    def ts(t):
        sleep(float(t))
    print('请输入要注册次数')
    num = int(input())
    print('数据加载中')
    #获取屏幕分辨率
    width,height = size()
    #获取对比值
    x1,y1 = float(width / 1920),float(height / 1080)
    #x1,y1 = 1.89,1.31
    #创建空列表用来保存坐标组
    xylist = []
    #读取坐标
    with open('坐标.json','r',encoding='utf-8') as f:
        xyjson = f.read()
        xyjson = loads(xyjson)

    #遍历坐标字典
    for i in range(len(xyjson)):
        x,y = xyjson[i]['x'],xyjson[i]['y']
        #将坐标转化为组
        xylist.append([x,y])

    print('数据加载50%')
    #获取用户名
    with open('userjson7.json', 'r', encoding='utf-8') as fs:
        t3 = fs.read()
        dicts = loads(t3)

    #获取图片
    shotlist = []
    with open('step.json','r',encoding='utf8') as f:
        d = f.read()
        d = loads(d)

    #遍历坐标字典
    for i in range(len(d)):
        shotname,shotimg,shotnum,shottime  = d[i]['name'],d[i]['img'],d[i]['num'],d[i]['time']
        #print(shotname)
        #将坐标转化为组
        shotlist.append([shotname,shotimg,shotnum,shottime])

    #加载time
    with open('time.json','r',encoding='utf8') as f:
        times = f.read()
        times = loads(times)
    #遍历时间
    ltimes = []
    for i in range(len(times)):
        ltime = times[i]['s']
        ltimes.append(ltime)

    print('数据加载100%')
    def imgzh(x):
        i = 1
        wait = 0
        while i == 1:
            coords = locateCenterOnScreen(x[1])  # 返回image屏幕上中心的（x，y）坐标
            if coords == None:
                print(f'{x[0]}没找到内容')
                if wait == int(x[2]):
                    print('跳出')
                    break
                else:
                    print('没找到内容')
                    #sleep(1)
                    wait += 1
                    i = 1
            else:
                click(coords)
                print(f'{x[0]}点击成功')
                i = 2
        #sleep(x[3])


    print('数据加载完成')
    #开启注册时间等待
    ts(ltimes[0])
    #sleep(3)
    for hs in range(num):
        print(f'在进行第{hs+1}注册')
        name4 = choice(dicts)
        txname1 = name4['name']
        fanbook_name = txname1
        touxiang = imgfile(fanbook_name)

        openchrome()
        main()
except Exception as e1:
    print("except:", e1)
    e1 = str(e1)
    with open('err.txt','w',encoding='utf8') as ff:
        ff.write(e1)
        ff.close()
        print('错误收集完毕')










