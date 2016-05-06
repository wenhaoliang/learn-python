# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，
# 查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。
# 写代码，对每月通话时间做个统计

import datetime

def statistics_month_time():
    dic = {}
    wb = xlrd.open_workbook("./0020/0020.xls")
    sheet = wb.sheets()[0]
    row_count = sheet.nrows

    for i in range(1, sheet.nrows):
        values = sheet.row_values(i)
        ym_str = values[2][:6]

        time_str = values[3]
        if '时' in time_str:
            time_str = re.sub('时', '.', time_str)
        if '分' in time_str:
            time_str = re.sub('分', '.', time_str)
        if '秒' in time_str:
            time_str = re.sub('秒', '', time_str)

        tmp = time_str.split('.')
        j = len(tmp) - 1
        sum = int(tmp[j])
        while j > -1:
            sum = sum + (len(tmp) - 1 - j) * 60 * int(tmp[j])
            j = j - 1

        if ym_str in dic:
            dic[ym_str] = dic[ym_str] + int(sum)
        else:
            dic[ym_str] = int(sum)

        # i = i + 1

    return dic
