
---
title: 'spawn git ENOENT解决方法  '
date: 2016-08-24 09:31:55
tags: git 错误
---

最近在部署hexo的时候出现了

    spawn git ENOENT
的错误，搜了下找到了解决方法，原来是git的环境变量(path)不知为何没有了，在win环境下因为git安装时是自动安装的，所以安装在哪里也不知道，只好去下载个Everything，轻松的找到了git的位置，然后把其添加到path中就解决了这个问题。
![附一个Everything图][1]
这里给出Everything的官方下载地址：[http://www.voidtools.com/][2]
下载时注意自己电脑是X86还是X64的。

  [1]: http://i2.buimg.com/567571/713ee6e9270e39eb.png
  [2]: http://www.voidtools.com/