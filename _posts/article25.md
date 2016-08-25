---
title: '安装自己喜欢的主题 '
date: 2016-08-24 12:51:52
tags: github hexo 博客
---

本篇来讲解如何安装自己喜欢的主题！
我们刚才使用Hexo生成的博客使用的是Hexo的默认主题：Landscape。怎么说呢，这个主题猛地一看还行，仔细一看还不如猛地一看，所以我决定另寻归宿。
<!--more-->

----------


安装yilia主题
========

选择主题
----

我们刚才使用Hexo生成的博客使用的是Hexo的默认主题：Landscape。怎么说呢，这个主题猛地一看还行，仔细一看还不如猛地一看，所以我决定另寻归宿。

可以在这里[hexo主题总站][1]寻找自己喜欢的主题，我在这里推荐一个主题
[yilia主题][2]，也就是我正在用的主题，简洁大方，比较符合我的品位；

当然，每个人的品位都不一样，你也可以选择其它的主题，当然也欢迎你选择yilia主题，这样就能继续一起愉快地折腾啦。

安装yilia主题
---------

Hexo 有两份主要的配置文件（_config.yml），一份位于站点根目录下，另一份位于主题目录下。为了描述方便，在以下说明中，将前者称为 站点配置文件，后者称为 主题配置文件。

下载 yilia 主题
-----------

使用 Git Shell 进入 Hexo 文件夹，输入以下两条命令：

    cd Hexo
    git clone https://github.com/litten/hexo-theme-yilia.git themes/yilia

    

启用yilia主题
--------

下载完成后，打开 站点配置文件，找到 theme 字段，并将其值更改为 yilia。

验证主题是否启用
--------

执行上面发博文的命令，刷新你的个人博客，就能看到你设置的主题是否启用。

个性化配置
----

菜单配置在 主题配置文件 的 menu，下面是我的菜单配置示例：
也可以去这个主题的创始人那里学习如何个性化配置[yilia主题创始人的网站][3]
```
# Header
menu:#这里是主页菜单的内容
  主页: /
  所有文章: /archives
 # 随笔: /tags/随笔

# SubNav
subnav:#在这里可以将我的网址改成你自己的
  github: "https://github.com/wenhaoliang"
  #weibo: "http://m.weibo.cn/u/5229251424"
  rss: /404.html
  zhihu: "https://www.zhihu.com/people/da-lan-chong-5"
  #douban: 
  #mail: "641541452@qq.com"
  #facebook:
  #google: 
  twitter: 
  #linkedin: 
  #qq: 'http://wpa.qq.com/msgrd?v=3&uin=641541452&site=qq&menu=yes'
  #rss: /404.html

# Content
excerpt_link: more
fancybox: true
mathjax: true

# 是否开启动画效果
animate: true

# 是否在新窗口打开链接
open_in_new: false

# Miscellaneous
google_analytics: ''
favicon: /favicon.ico

#你的头像url，输入你头像的图片的url地址
avatar: "https://avatars1.githubusercontent.com/u/11350373?v=3&s=460"
#是否开启分享
share_jia: false
share_addthis: false
#是否开启多说评论，填写你在多说申请的项目名称 duoshuo: duoshuo-key
#若使用disqus，请在博客config文件中填写disqus_shortname，并关闭多说评论
#关于这个多说评论框我在下篇文中讲解
duoshuo: true
#是否开启云标签
tagcloud: hahaha

#是否开启友情链接
#不开启——
#friends: false
#开启——
friends:
  Rehack: http://www.rehack.cn/	
  我思故我在: http://artinhuang.com/
  给时光以生命: http://kingname.info/
  青春样: http://www.qcyoung.com/
  黄卯卯的小站: http://huangjinyuan.xyz/
#是否开启“关于我”。
#不开启——
#aboutme: false
#开启——
aboutme: 懒
```
这样就安装主题完成了~

  [1]: https://github.com/hexojs/hexo/wiki/Themes
  [2]: https://github.com/litten/hexo-theme-yilia
  [3]: http://litten.github.io/2014/08/31/hexo-theme-yilia/
  [4]: http://duoshuo.com31/hexo-theme-yilia/