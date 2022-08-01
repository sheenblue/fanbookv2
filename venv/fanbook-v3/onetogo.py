import txname
import fanbookv2
import newphone
import addsql
import readxls


for i in range(1):
    phone = newphone.Newphone() #生成一个新手机号
    #写入数据库
    con = addsql.sql_connection()
    phonenum = int(phone)
    query = (phonenum,)  # 删除的数据是元组类型，因此1后面应该有逗号，修改后cur.execute(sql,(1,)，可以成功执行；
    t = addsql.sql_fetch(con, query, phonenum)
    if t == False:
        print(t)
        #生成头像和名字
        tname = txname.main() #获取一个名字列表
        fname = txname.txname2(tname) #随机取一个名字
        txpath = txname.imgfile(fname) #用上面的名字生成图片地址

        #生成六个动作组
        action1 = readxls.sheets(0)
        action2 = readxls.sheets(1)
        action3 = readxls.sheets(2)
        action4 = readxls.sheets(3)
        action5 = readxls.sheets(4)
        action6 = readxls.sheets(5)
        action7 = readxls.sheets(6)

        fanbookv2.onestep(action1)
    else:
        print('终止程序')
        break