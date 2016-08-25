---
title: 'github + hexo 建立你的第一个博客 '
date: 2016-08-24 10:03:50
tags: github hexo 博客
---

前言
其实呢，建立博客非常简单的(哈哈，不管什么东西，你会了觉得不管怎么样都简单，不会的不管怎么样的难)，我来给大家说说建立博客的几点步骤：

 1. 使用GitHubPages和Hexo建立自己的博客
 2. 安装自己喜欢的主题
 3. 购买域名并绑定
 4. 安装多说评论框

**这里面也就第二项的难度较大，但是不要怕，我会一步一步的给大家完成指导的，如果有任何问题也可以随时联系我，我会尽力给大家解决的！**
<!--more-->

----------


**下面先介绍为何选择GitHubPages和Hexo来搭建博客，然后介绍搭建博客的详细过程。**

----------


why GitHub Pages and Hexo 
=========================================================

之前在关于我里面提到过，搭建博客会有三个阶段，我选择的是第三种方法。因为GitHub的存在，我们得以简单快速地搭建个人博客。
 GitHub
====
GitHub，是一个代码托管网站和社交编程网站。这里聚集了世界上各路技术牛叉的大牛，和最优秀的代码库。把你的博客托管在这里，还有什么不放心的呢O(∩_∩)O。
**GitHub Pages**
GitHub Pages，是用来托管GitHub上静态网页的免费站点，那GitHub Pages具体有哪些功能呢：

 - 有300M免费空间，资料自己管理，保存可靠；
 - 享受 GitHub 的便利，上面有很多大牛，眼界会开阔很多；
 - 可以使用很多现成的博客框架，搭建过程简单快速。

----------

HEXO
====

Hexo是一个简单、快速、强大的静态博客框架,出自台湾大学生tommy351之手。我也看过使用Jekyll、Octopress搭建个人博客的过程，确实要繁琐许多。相比之下Hexo更轻便更快捷，下面是Hexo官网强调Hexo的四大特点：

 - 极速生成静态页面
 - 一键部署博客
 - 丰富的插件支持
 - 支持Markdown


----------
相信大家对GitHub Pages和Hexo有了一定的了解，下面进入正题。

使用GitHub Pages建立博客站点
====================

注册GitHub

访问GitHub,注册十分简单，一定要记住注册时使用的邮箱，因为 GitHub 上很多通知都是通过邮箱的。如下图所示：
![注册github账号][1]
申请成功后，在GitHub官网上登录，并验证邮箱即可。

在GitHub上建立仓库

与 GitHub 建立好连接之后，就可以方便的使用它提供的 Pages 服务，GitHub Pages 分两种，一种是用你的GitHub用户名建立的username.github.io这样的用户&组织站点，另一种是依附项目的Pages。

想建立个人博客是用的第一种，形如username.github.io这样的可访问的站点，每个用户名下面只能建立一个。如下图所示：
![建立仓库1][2]
![建立仓库2][3]

关于Github的使用，我的老师Crossin先生也写了一篇通俗易懂的教程，大家可以去看看[极简 Github 上手教程][4]

----------


搭建环境
====

安装软件
----

Node.js
========
Node.js下载地址
[Node.js][5]
下载完成后根据提示一步一步安装就好，这个没有什么需要特别说明的
GitHub for Windows下载地址
[GitHub for Windows][6]
这里有一点说明，下载这个github时因为是先从官网下载下来了一个下载器，然后再在本地下载，因为是外网，可能有点卡，所以下载好了全部并整理好了离线版本，你下载这个直接就自动安装了：
[github离线版][7]
**密码：olr2**

下载并安装下面两个软件，一直点击下一步即可：

使用GitHub for Windows登录GitHub
----------------------------
![使用GitHub for Windows登录GitHub][8]
![使用GitHub for Windows登录GitHub][9]
![使用GitHub for Windows登录GitHub][10]

配置SSH Key
====================

我们如何让本地git项目与远程的GitHub建立联系呢？用SSH key。在桌面或开始菜单中找到 Git Shell，打开后输入以下命令：

    ssh -T git@github.com

如图：
![ssh -T git@github.com][11]
如果是下面之类的反馈（或者显示 Hi xxx）：

    The authenticity of host 'github.com (207.97.227.239)' can't be established. RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48. Are you sure you want to continue connecting (yes/no)?

不用紧张，输入 yes 之后,看到下图的结果，就配置成功了：
![不用紧张，输入 yes 之后,看到下图的结果，就配置成功了][12]


----------


使用Hexo创建博客框架
============

Hexo安装
------

打开 Git Shell，启动后依次输入以下命令：

    cd /
    npm install hexo-cli -g

如图：
![提示：cd / 作用是返回根目录，Git Shell 默认装在 C盘，启动时默认路径为 C:\Users\xxx(用户名)\Documents\GitHub，输入 cd / 命令后就返回到了 C盘根目录下，需不需要使用 cd / 看个人习惯（下同）][13]
**提示：cd / 作用是返回根目录，Git Shell 默认装在 C盘，启动时默认路径为 C:\Users\xxx(用户名)\Documents\GitHub，输入 cd / 命令后就返回到了 C盘根目录下，需不需要使用 cd / 看个人习惯（下同）**

Hexo部署
======

Hexo的部署可采用如下方法，输入命令： hexo init [文件名]。

打开Git Shell，启动后依次输入以下命令：

    cd /
    hexo init Hexo

回车后出现该提示则表示正确：
![部署成功之后，Hexo 会自动在目标文件夹建立博客网站所需要的所有文件。此时可以通过输入以下命令在本地进行预览（在刚才创建的文件夹里）：][14]
**部署成功之后，Hexo 会自动在目标文件夹建立博客网站所需要的所有文件。此时可以通过输入以下命令在本地进行预览（在刚才创建的文件夹里）：**

    hexo generate 
    hexo server
系统可能会出现提示，请点击允许。如下图所示则表示正确：
![系统可能会出现提示，请点击允许。如下图所示则表示正确][15]
此时打开浏览器，在浏览器地址栏输入 http://localhost:4000/ （默认端口为4000）, 便可以看到最原始的博客了。以后发表博文想先预览，也可以通过 hexo server 在本地先跑起来，看看效果。

效果如下图所示：
![恭喜，到目前为止个人博客的雏形已经有了。][16]

**恭喜，到目前为止个人博客的雏形已经有了。**
在 Git Shell 中按 Ctrl + C 并输入 y 可以停止该服务。


----------


将本地文件部署到 GitHub
===============

修改 Hexo 中的 _config.yml 文件

在 Hexo 文件夹下找到 _config.yml 文件,如下图所示：
![_config.yml 文件][17]
找到其中的 deploy 标签，改成下图所示形式，并保存。注意：冒号后面要加上一个空格，否则会报错。
![冒号后面要加上一个空格，否则会报错。][18]


----------


将其 deploy 到仓库中
--------------

打开 Git Shell 进入创建的文件夹，依次输入以下命令：


    hexo clean
    hexo generate
    hexo deploy

如果出现下图错误，不要着急：

![如果出现下图错误，不要着急][19]
将deploy 的 type 改成 git，然后再在 Git Shell 中运行以下命令:

    npm install hexo-deployer-git --save
再重新来一遍：

    hexo clean
    hexo generate
    hexo deploy

出现以下提示则表示正确：
![出现以下提示则表示正确][20]

**恭喜，到这一步，个人博客就已经部署到 GitHub 上了，你可以到你的GitHub仓库查看是否已经更新。此时,通过 your_user_name.github.io（即你那个仓库的名称，形如：”你的 GitHub 用户名”.github.io）,就可以看到你的个人博客了。**

PS
==
这里可能会出现这种需要输入账号密码的情况
![这里可能会出现这种需要输入账号密码的情况](http://i1.buimg.com/567571/025eb4fa49f2a8e8.png)
输入github的账号密码就可以了，记住那里输入密码的时候光标是不会移动的，只要你输入了就好，不要以为没输入上~哈哈哈
----------


----------

发表博文
====

辛苦了这么久，终于回到我们搭建博客最初的目标–写作，现在来看看怎么写博文并发表吧(^__^)。

新建博文
====
我们可以使用命令新建一篇博文,使用 Git Shell 进入 Hexo 文件夹，输入以下命令：

    hexo new "文章题目"

====
命令执行完后，就会发现在 Hexo\source_posts 目录中多了一个文件博文名.md，这就是我们刚才新建的博文。

此外，我们也可以直接进入 Hexo\source_posts 目录中，右键新建一个文本文档，将名字改为博文名.md,这样也新建了一篇博文。

新建页面
====
上面新建的博文是显示在单个文章界面，这里新建的页面是作为单个页面显示的，比如下图的分类、标签、归档和关于我，你点击后都是显示为单个页面。
![新建页面][21]
你只需要记住新建博文是用上面的方法，新建页面是用这里的方法就行了，这里也采用命令新建页面：

    hexo new page "页面名称"

命令执行完后，就会发现在在 Hexo\source 目录中多了一个文件夹，里面还有一个index.md,这就代表我们新建了一个页面。

写博文
===

用文本编辑器打开上面新建的博文，如下图所示：
![用文本编辑器打开上面新建的博文][22]
新建的页面略有不同，没有tags和categories标签。

三个”-“后面就是博文的正文内容，接下来就是正儿八经地撰写博文了。

因为我们的博文都是用Markdown语言写的，所以首先，你需要一个好用的Markdown编辑器。其实好用的Markdown编辑器一大堆，这里就给大家推荐两个，如果你用的不习惯也可以换其它的。

 - 本地编辑器：Haroopad,非常小众的一款Markdown编辑器，左边编辑右边实时预览效果，非常轻便；
 - 在线编辑器：MaHua,也是比较小众的一款Markdown编辑器，但效果确实很棒，我的这篇博文就是用MaHua写的。

现在你可以打开新建的博文了，然而还不造怎么下手对吧。其实很简单，除了特殊格式，其它的你就当做在word里面写文章就行了，具体请看这里的Markdown教程：[Markdown——入门指南][23]。

发博文
===

呼啦啦，博文写好了，你得发表出去别人才看得到呀。依然在 Git Shell 中进入 Hexo 文件夹，执行下面几条命令，将博客部署到 GitHub 上：

    hexo clean
    hexo generate
    (若要本地预览就先执行 hexo server)
    hexo deploy

快捷命令：

    hexo g == hexo generate
    hexo d == hexo deploy
    hexo s == hexo server
    hexo n == hexo new

# 还能组合使用，如：

    hexo d -g

刷新你的个人博客，就可以看到新鲜出炉的博文了，赶紧邀请小伙伴们来欣赏吧。


----------
一个可能出现的错误 

    spawn git ENOENT

 解决方法在这里[spawn git ENOENT解决方法][24]


  [1]: http://7xnuu7.com1.z0.glb.clouddn.com/blogsignupGithub.png
  [2]: http://i2.buimg.com/567571/38140d1cf579451d.png
  [3]: http://i2.buimg.com/567571/dee612c2a95f3259.png
  [4]: http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&tempkey=RGC3FECNbCPVJZAJADDUnslgBUIqYPNgJ6NstBxRiWN6Oc2ASwak8gzRjgtTq6Mu5qSWAKEDRMyzSSiHk18WvjTH0tDh6FozXCyMy9kUVW/MG4WFGI8PDJUpGjN%2bXAV5SiNhJ0C0nq0%2bpDHwRPlOCg==&#rd
  [5]: https://nodejs.org/en/
  [6]: https://desktop.github.com/
  [7]: http://pan.baidu.com/s/1bZthpW
  [8]: http://7xnuu7.com1.z0.glb.clouddn.com/blogsignin1.png
  [9]: http://i2.buimg.com/567571/fd88d8ff20ac2204.png
  [10]: http://i2.buimg.com/567571/1c88bbfb31c0b227.png
  [11]: http://7xnuu7.com1.z0.glb.clouddn.com/blogssh1.png
  [12]: http://7xnuu7.com1.z0.glb.clouddn.com/blogssh2.jpg
  [13]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo1.jpg
  [14]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo2.png
  [15]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo4.jpg
  [16]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo5.png
  [17]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo6.png
  [18]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo7.png
  [19]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo8.png
  [20]: http://7xnuu7.com1.z0.glb.clouddn.com/bloghexo9.jpg
  [21]: http://7xnuu7.com1.z0.glb.clouddn.com/blogwrite1.png
  [22]: http://7xnuu7.com1.z0.glb.clouddn.com/blogwrite2.png
  [23]: http://www.jianshu.com/p/1e402922ee32/#
  [24]: http://liangwenhao.cn/2016/08/24/spawn%20git%20ENOENT%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/