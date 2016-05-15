#coding:utf-8
import urllib
import urllib2
import re

#处理页面标签
class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|<p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br>|<br><br>')
    replaceExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, '', x)
        x = re.sub(self.removeAddr, '', x)
        x = re.sub(self.replaceLine, '\n', x)
        x = re.sub(self.replaceTD, '\t', x)
        x = re.sub(self.replacePara,'\n       ', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.replaceExtraTag, '', x)
        return x.strip()


class BDTB:

    def __init__(self, baseURL, seeLZ, floorTag):
        self.baseURL = baseURL
        self.seeLZ = "?see_lz=" + str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.defaultTitle = u"百度贴吧"
        self.floor = 1
        self.floorTag = floorTag


    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"该网页获取不到呢，错误原因是", e.reason
                return None


    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None


    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item)+ '\n'
            contents.append(content.encode('utf-8'))
        return contents


    def setFileTitle(self, title):
        if title is not None:
            self.file = open(title + ".txt" , "w+")
        else:
            self.file = open(self.defaultTitle + '.txt', "w+")

    def writeData(self,contents):
        for item in contents:
            if self.floorTag == "1":
                floorLine =  '\n' +str(self.floor) + u"---------------------------------------念念最漂亮了--------------------------------------\n"
                self.file.write(floorLine.encode('utf-8'))
            self.file.write(item)
            self.floor += 1


    def start(self):
        indexPage = self.getPage(1)
        title = self.getTitle(indexPage)
        pageNum = self.getPageNum(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print u"该网页已经失效了哦"
            return None
        try:
            print u"该网页一共有" + str(pageNum) + u"页哦~"
            for i in range(1, int(pageNum) + 1):
                print u"正在写入第" + str(i) + u"页哦，请稍安勿躁"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError,e:
            if hasattr(e, "reason"):
                print u"出错了呢，错误原因是：",e.reason
                return
        finally:
            print u"任务完成了哦，请享受它吧~"


if __name__ == "__main__":
    print u"请输入帖子代号"
    baseURL =  'http://tieba.baidu.com/p/' + str(raw_input())
    seeLZ = raw_input('是否只获取楼主发言，是输入1，否输入0\n')
    floorTag = raw_input('是否写入楼层信息，是输入1，否输入0\n')
    data = BDTB(baseURL, seeLZ, floorTag)
    data.start()















