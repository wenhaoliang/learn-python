#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自动填问卷星（http://www.sojump.com）
复杂的题目类型
"""
# 举例： http://www.sojump.com/jq/4738641.aspx
# 注意：该页面添加了验证码，所以此程序已经失效

# 题与题之间以 '{' 分隔，序号与答案以 ‘$‘ 分隔
# 输入类型      表示方式         解释
# 多选         1｜2｜3｜4      答案以 '｜' 号分隔
# 填空         shiyanlou      答案就是字符串
# 下拉选择          2         答案就是序列号，和单选是一样一样的
# 选择＋填空   5^shiyanlou    序号和填空间加^就行


import re
from urllib import request, parse
from time import time, strftime, localtime


class Sojump(object):
    def __init__(self, jq_url):
        self.answer_list = []
        self._uri_param = {}
        self._jq_url = jq_url
        self._jq_base = "http://www.sojump.com"
        self._uri_base = "http://www.sojump.com/jq/8661167.aspx?{}"
        self._jq_sum = 0
        self._init_param()

    @staticmethod
    # 返回submitdata字符串（单选为例）
    # ([(1,2),(2,4),(3,1)]) => '1$2}2$4}3$1'
    def gen_post_string(answer):
        def concat_pair(pair):
            return '$'.join([str(pair[0]), str(pair[1])])

        tmp_list = []
        for x in answer:
            tmp_list.append(concat_pair(x))
        return '}'.join(tmp_list)

    def _init_param(self):
        resp = request.urlopen(self._jq_url)
        text = resp.read().decode()

        self._jq_sum = int(re.findall(r'div(\d+)', text)[-1])  # 取最后一个
        self._uri_param['submittype'] = '1'
        self._uri_param['t'] = str(int(time() * 1000))
        self._uri_param['starttime'] = strftime("%Y/%m/%d %H:%M:%S", localtime())
        self._uri_param['rn'] = re.search(r'rndnum="(\d+)(.\d*)*"', text).group(1)
        self._uri_param['curID'] = re.search(r'(\d+).aspx', resp.geturl()).group(1)

    def submit(self):
        if len(self.answer_list) == self._jq_sum:
            answer = zip(range(1, self._jq_sum + 1), self.answer_list)
            post_data = parse.urlencode({'submitdata': self.gen_post_string(answer)})
            get_data = parse.urlencode(self._uri_param)
            request_url = self._uri_base.format(get_data)
            req = request.Request(request_url, post_data.encode())
            self._result = request.urlopen(req)
        else:
            print("Error:the length of answer list doesn't match")

    def redirect_url(self):
        path = re.search(r'(/wjx.*)', self._result.read().decode())
        # self._result.read().decode() 的内容为：您输入的验证码有误，请重新输入！
        # 程序在此失效
        #print(self._jq_base + path)


if __name__ == '__main__':
    sj = Sojump("http://www.sojump.com/jq/4738641.aspx")
    sj.answer_list = [2, 1, '2|3', 5, '3|4', '1^hello', 'shiyanlou', 2]
    for x in range(1, 10):
        sj.submit()
        sj.redirect_url()