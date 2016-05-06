# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0015 题： 纯文本文件 city.txt为城市信息,写到 city.xls 文件中
import json
import xlwt

def dictxt_to_xls(file_path=None):
    if file_path is None:
        return

    file = open(file_path, 'r')
    if file is None:
        return

    content = json.loads(file.read())
    list_data = sorted(content.items(), key=lambda d:d[0])

    (path, name)=os.path.split(file.name)
    file_name = name.split('.')[0]

    wb = xlwt.Workbook()
    ws = wb.add_sheet(file_name)

    row = 0
    for item in list_data:
        col = 0
        ws.write(row, col, item[0])
        col += 1

        value = item[1]
        if type(value) == list:
            for obj in value:
                ws.write(row, col, obj)
                col += 1
        else:
             ws.write(row, col, value)
        row += 1

    save_path = path + "/" + file_name + ".xls"
    wb.save(save_path)
