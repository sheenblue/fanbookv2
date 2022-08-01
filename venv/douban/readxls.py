import xlrd


# 获取所有列
def rowlist(t):  # t是表名
    rowlist = []
    data = xlrd.open_workbook(f'{t}.xls')
    sheet = data.sheet_by_index(0)
    nrows = sheet.nrows
    for row in range(nrows):
        # print(sheet.row_values(row))
        rowlist.append(sheet.row_values(row))  # 获取第几行数据
    return rowlist


# 获取所有行数据
def sheets(t):  # t是数字，表示第几个工作簿
    rowlist = []
    data = xlrd.open_workbook('step02.xls')
    sheet = data.sheet_by_index(t)
    nrows = sheet.nrows
    for row in range(nrows):
        # print(sheet.row_values(row))
        rowlist.append(sheet.row_values(row)) #获取第几行数据
    return rowlist


if __name__ == '__main__':
    t = '试炼'
    t = rowlist(t)
    print(t)













