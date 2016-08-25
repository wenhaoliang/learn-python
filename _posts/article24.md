---
title: '安装多说评论框 '
date: 2016-08-24 13:52:55
tags: github hexo 博客 多说
---
首先登陆多说官网[多说][1]使用QQ账号直接登陆
然后![](http://i2.buimg.com/567571/ad363d8d374bd365.png)
<!--more-->
![](http://i1.buimg.com/567571/f40ef12a1ee20233.png)
打开hexo文件夹中_config.yml并添加添加多说的配置：

      duoshuo_shortname: 你站点的short_name
例如![](http://i1.buimg.com/567571/4117671915bc3015.png)
然后打开themes\landscape\layout\_partial\article.ejs
![](http://i1.buimg.com/567571/99ca2173dc817c1a.png)
去掉之后把你刚才复制的东西粘贴到这个位置，然后就大功告成了~~

  [1]: http://duoshuo.com/