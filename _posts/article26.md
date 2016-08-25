---
title: '购买并绑定域名 '
date: 2016-08-24 13:35:06
tags: github hexo 博客 购买域名
---

哈哈，震撼人心的时刻终于到来了，之前一直都是用的GitHub的二级域名，总有一种又臭又长的感觉。现在，我们就来看看怎么购买自己喜欢的个性化域名，并绑定到你的个人博客上面去。当然，不想花钱购买域名的同学，可以跳过这个步骤，GitHub 提供的二级域名[username.github.io]，平常自己写写博客也够用了。
<!--more-->
购买域名
----

经过广大网友的推广，我们选择使用阿里云购买域名。
[阿里云][1]
![购买步骤1](http://i2.buimg.com/567571/814726158eb769d4.png)
![购买步骤2](http://i2.buimg.com/567571/653b1bc34c4f845d.png)
![购买步骤3](http://i2.buimg.com/567571/f90c4fa05cd6ba74.png)
之后就进入付款界面进行付款

将个人域名与 GitHub Pages 的空间绑定
-------------------------

在 Hexo\source 文件夹里新建一个名为 CNAME 的文件，用文本编辑器打开，添加内容 yourwebsite.com （你刚才购买的个人域名 ）。保存后，部署你的博客即可。

DNS设置
-----

同样经过广大网友的推广， 我选择[DNSpod][2]来设置DNS,速度快、免费、且稳定。

注册DNSpod，添加域名，如下图设置:
![DNSpod](http://i4.buimg.com/567571/1c0db88150de09c6.png)

DNSpod1
-------

其中两条A记录指向的IP地址是GitHub Pages的提供的IP:

 - 192.30.252.153
 - 192.30.252.154

如果博客不能访问，有可能是GitHub更改了空间服务的ip地址，及时到[GitHub Pages][4]查看最新的IP即可。

www指定的记录是你在GitHub托管博客的仓库。

去阿里云修改DNS地址
-----------
![点击管理](http://i4.buimg.com/567571/132686c81d9ab4cc.png)
![点击修改DNS](http://i4.buimg.com/567571/fc8bcc2f86844cfb.png)
![修改成这个样子](http://i4.buimg.com/567571/34f7498b512d7dee.png)

如果还有疑问可以看：DNSpod提供的官方帮助。

提示：设置DNS之后短时间内可能无法访问你的个人博客，因为要等待全球递归DNS服务器刷新（最多72小时），不过没问题的话几小时内就可以访问了。


----------

恭喜你
===

到现在就完成了！


  [1]: https://wanwang.aliyun.com/?spm=0.0.0.0.qwCJNS
  [2]: https://www.dnspod.cn/
  [3]: http://7xnuu7.com1.z0.glb.clouddn.com/blogdnspod1.png
  [4]: https://help.github.com/articles/tips-for-configuring-an-a-record-with-your-dns-provider/