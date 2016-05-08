# coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
 
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
 
    def __unicode__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.title