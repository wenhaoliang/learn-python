# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0016 题： 纯文本文件 numbers.txt, 请将上述内容写到 numbers.xls 文件中
def listtxt_to_xls(file_path=None):
    if file_path is None:
        return

    file = open(file_path)
    if file is None:
        return

    content = json.loads(file.read())
    content.sort(key=lambda x:x[0])

    (path, name)=os.path.split(file.name)
    file_name = name.split('.')[0]
    wb = xlwt.Workbook()
    ws = wb.add_sheet(file_name)

    for i in range(len(content)):
        col = 0
        list = content[i]
        for value in list:
            ws.write(i, col, content[i][col])
            col += 1

    save_path = path + "/" + file_name + ".xls"
    wb.save(save_path)
# pip3 install xlrd
import xlrd
def read_xls(file_path=None):
    if file_path is None:
        return None

    data_list = {}
    wb = xlrd.open_workbook(file_path)
    sheet_names = wb.sheet_names()
    for name in sheet_names:
        table = wb.sheet_by_name(name)
        table_data = []
        for i in range(table.nrows):
            row_data = table.row_values(i)
            table_data.append(row_data)

        data_list[name] = table_data

    return data_list
