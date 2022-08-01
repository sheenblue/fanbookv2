import csv

def creatcsv(t):
    with open(f'{t}.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(['书名','作者','出版社','简介'])
    print('创建成功')


def xieru(t,y):
    with open('book.csv','a',errors='ignore',newline='') as f:
        fieldnames = ['书名','作者','出版社','简介']
        writer =csv.DictWriter(f,fieldnames=fieldnames)
        writer.writerow(t)
    print(f'【{y}】写入成功')

if __name__ == '__main__':
    #creatcsv('book')
    t = {"书名":"1",
         "作者":"2",
        "出版社":"3",
        "简介":"4"}
    xieru(t)