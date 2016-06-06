#-*- coding:utf8 -*-
import urllib, urllib2, random, re
from time import localtime, strftime, time

class Sojump(object):

    def __init__(self, jq_url):
        self.answer_list = []
        self._uri_param = {}
        self._jq_url = jq_url
        self._jq_base = "http://www.sojump.com"
        self._uri_base = "http://www.sojump.com/handler/processjq.ashx?{}"
        self._jq_sum = 0
        self._init_param()

    @staticmethod
    def gen_post_string(answer):
        def concat_pair(pair):
            return '$'.join([str(pair[0]), str(pair[1])])

        tmp_list = []
        for x in answer:
            tmp_list.append(concat_pair(x))
        return '}'.join(tmp_list)

    def _init_param(self):
        response = urllib2.urlopen(self._jq_url)
        text = response.read();

        self._jq_sum = int(re.findall('div(\d+)',text)[-1])
        self._uri_param['submittype'] = '1'
        self._uri_param['t'] = str(int(time()*1000))
        self._uri_param['starttime'] = strftime("%Y/%m/%d %H:%M:%S", localtime())
        self._uri_param['rn'] = re.search('rndnum="(\d+)"', text).group(1)
        self._uri_param['curID'] = re.search('(\d+).aspx',response.geturl()).group(1)

    def submit(self):
        if len(self.answer_list) == self._jq_sum:
            answer = zip(range(1,self._jq_sum+1),self.answer_list)
            post_data = urllib.urlencode({'submitdata':self.gen_post_string(answer)})
            get_data = urllib.urlencode(self._uri_param)
            request_url = self._uri_base.format(get_data)
            request = urllib2.Request(request_url, post_data)
            self._result = urllib2.urlopen(request)
        else:
            print "Error:the length of answer list doesn't match"

    def redirect_url(self):
        path = re.search('(/wjx.*)',self._result.read()).group(0)
        print self._jq_base + path

    def question_sum(self):
        return self._jq_sum


if __name__ == '__main__':
    sj = Sojump("http://www.sojump.com/jq/4738641.aspx")
    sj.answer_list = [2, 1, '2|3', 5, '3|4', '1^hello', 'shiyanlou', 2]
    for x in xrange(1,10):
        sj.submit()
        sj.redirect_url()