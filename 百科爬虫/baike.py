# coding:utf8

from bs4 import BeautifulSoup
import re
import urlparse
import urllib2
import os

#URL管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            raise Exception # 为None抛出异常
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            raise Exception # 为None抛出异常
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
#HTML下载器
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()
# HTML解析器
class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
        new_urls = []   ###########
        # /view/123.htm： 得到所有词条URL
        links = soup.find_all("a", href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link["href"]
            #把new_url按照page_url的格式拼接成完整的URL格式
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.append(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}
        #url
        res_data["url"] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summery_node = soup.find("div",class_="lemma-summary")
        res_data["summary"] = summery_node.get_text()
        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

# HTML输出器
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open(u'百度百科爬取结果.html','w')
        
        fout.write("<html><meta charset=\"utf-8\" />")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()

class SpiderMain():
    def craw(self, root_url, page_counts):
        count = 1   #记录爬取的是第几个URL
        UrlManager.add_new_url(root_url)
        while UrlManager.has_new_url():    # 如果有待爬取的URL
            try:
                # 把新URL取出来
                new_url = UrlManager.get_new_url()
                # 记录爬取的URL数量
                print u"\n这是第 %d个网站 : %s" % (count, new_url)
                # 下载该URL的页面
                html_cont = HtmlDownloader.download(new_url)
                # 进行页面解析，得到新的URL和数据
                new_urls, new_data = HtmlParser.parse(new_url, html_cont)
                # 新URL补充进URL管理器
                UrlManager.add_new_urls(new_urls)
                # 进行数据的收集
                HtmlOutputer.collect_data(new_data)

                # 爬取到第counts个链接停止
                if count == page_counts:
                    break
                count = count + 1
            except:
                print "craw failed"

        #输出收集好的数据
        HtmlOutputer.output_html()

if __name__=="__main__":
    print u"\n欢迎来到百度爬虫:)"
    
    UrlManager = UrlManager()
    HtmlDownloader = HtmlDownloader()
    HtmlParser = HtmlParser()
    HtmlOutputer = HtmlOutputer()

    root = raw_input( u"请输入您想要爬的网站后缀: http://baike.baidu.com/view/".encode('gbk'))
    root_url = "http://baike.baidu.com/view/%s" % (root)  #爬虫入口URL
    page_counts = input(u"请输入您想要爬取得数量:".encode('gbk') )  #想要爬取的数量

    SpiderMain = SpiderMain()
    SpiderMain.craw(root_url,page_counts)   #启动爬虫

    print u"\n我已经爬完了全部内容啦！结果保存在： "+os.path.dirname(os.path.abspath('__file__')) + u"\百度百科爬取结果.html"