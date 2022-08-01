from json import loads



#随机取名和头像
def txname2(dicts):
    name4 = choice(dicts)
    txname1 = name4['name']
    return  txname1 #返回昵称
def imgfile(t):
    pwd = getcwd()
    txfile = f'{t}.jpg'

    txfile = join(pwd, 'tx','3', txfile)
    return txfile #返回头像路径

def main():
    with open('userjson7.json', 'r', encoding='utf-8') as fs:
        t3 = fs.read()
        dicts = loads(t3)

    return dicts

#先调用输出一个名单列表
#再调用输出名字和图片路径