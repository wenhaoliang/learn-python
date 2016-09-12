# -*- coding: utf-8 -*-
import scrapy
# from scrapy.http import FormRequest
# from scrapy.http import Request
# import math
import random

class VolunteerSpiderSpider(scrapy.Spider):
    name = "volunteer_spider"
    allowed_domains = ["sojump.com"]
    start_urls = (
        'http://www.sojump.com/m/8661167.aspx?',
    )
    multi_choice = [1,2,3,4]

    def parse(self, response):
        print '---------has fetch into the form web--------------'
        post_url = 'http://www.sojump.com//handler/processjq.ashx?submittype=1&curID=7315769&t=1457347143177&starttime=2016%2F3%2F7%2018%3A37%3A45&rn=1033949054'
        self.header = {
            'Host':'www.sojump.com',
            'Origin':'http://www.sojump.com',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Content-Type':' application/x-www-form-urlencoded',
            'Accept':'*/*',
            'Referer':'http://www.sojump.com/jq/7315769.aspx',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.8',
            'Connection':'close'
        }

        self.cookie = {
            '.ASPXANONYMOUS': 'dTv_ME2u0QEkAAAAZjk3YjQxZDUtNjBlYy00YTVmLTkwYzgtMDU1NWYzMDMyMDMySICELmArCd2neCK7R7WSsfQVsU81',
            'ASP.NET_SessionId':'k3sq4c45vwiifl554dgyaavv',
            'SojumpSurvey':'01027BA76281D245D308FE7B477408F445D308000D6500780070006C006F007200650072005F006C00690061006F0000012F00FF39937A3BF618273B36EC96EE24B846556FB87F45',
            'WjxUser':'UserName=499174318%40qq.com&Type=1',
            'hasShareBd':'1',
            'bdshare_firstime':'1457278250175',
            'LastActivityJoin':'',
            'CNZZDATA4478442':'cnzz_eid%3D1747491231-1457273995-%26ntime%3D1457277876'
        }


        for i in range(1,201,1):
            current_ans = self.generate_ans(i)
            print '!!!!!!!!the ans will post is %s!!!!!!!'%current_ans
            yield scrapy.FormRequest(url = post_url , cookies=self.cookie,
                                     headers=self.header,
                                     method='post',callback=self.after_post_form_parse,
                                     formdata = {'submitdata':str(current_ans)}
                                     )


    def after_post_form_parse(self,response):
        print 'post the form successed!!!!'
        print response.body
        # print 'get the cookie is %s'%response.meta['LastActivityJoin']
        # self.response_cookie = response.meta['LastActivityJoin']


    def generate_ans(self,current_num):
        final_ans = ''
        ans_form_str = '%d$%d}'
        ans_form_last_ans = '%d$%d'
        multi_form_ans = '%d$%s}'
        has_the_second_question = True
        if current_num%50 == 0:
            has_the_second_question = False
        print current_num,has_the_second_question
        for i in range(1,11,1):
            if i == 1 :
                question_id = 1
                question_ans = random.randint(1,5)
                final_ans += ans_form_str%(question_id,question_ans)

            elif i == 2 :
                question_id = 2
                question_ans = 1
                if has_the_second_question != True:
                    question_ans = 2
                final_ans += ans_form_str%(question_id,question_ans)

            elif i == 3 and has_the_second_question:
                question_id = 3
                question_ans = random.randint(1,5)
                final_ans += ans_form_str%(question_id,question_ans)

            elif i == 4 :
                question_id = 4
                question_ans = random.randint(1,4)
                final_ans += ans_form_str%(question_id,question_ans)

            elif i == 5 :
                question_id = 5
                question_ans = random.randint(1,2)
                final_ans += ans_form_str%(question_id,question_ans)

            elif i == 6 :
                question_id = 6
                question_ans = ''
                choice_num = random.randint(1,4)
                random.shuffle(self.multi_choice)
                the_ans = self.multi_choice[0:choice_num]
                question_ans += str(the_ans[0])
                for i in the_ans[1:choice_num]:
                    question_ans += '|'+str(i)
                final_ans += multi_form_ans%(question_id,question_ans)

            elif i == 7 :
                question_id = 7
                question_ans = random.randint(1,5)
                final_ans += ans_form_str%(question_id,question_ans)

            elif i == 8 :
                question_id = 8
                question_ans = ''
                choice_num = random.randint(1,4)
                random.shuffle(self.multi_choice)
                the_ans = self.multi_choice[0:choice_num]
                question_ans += str(the_ans[0])
                for i in the_ans[1:choice_num]:
                    question_ans += '|'+ str(i)
                final_ans += multi_form_ans%(question_id,question_ans)

            elif i == 9 :
                question_id = 9
                question_ans = random.randint(1,4)
                final_ans += ans_form_str%(question_id,question_ans)

            elif i == 10 :
                question_id = 10
                question_ans = random.randint(1,5)
                final_ans += ans_form_last_ans%(question_id,question_ans)

        return final_ans



