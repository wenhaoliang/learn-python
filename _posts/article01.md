
---
title: 'CSS中那些布局(三栏布局)  '
date: 2016-08-23 15:00:03
tags: 前端 html css
---



**最近在做IFE的前端任务，在前五个任务中分别使用了两栏布局和三栏布局，现在来整理一下。**
-----------------------------------------------

**三列自适应布局**
===========
除了常见的两列布局，我们也经常能够见到三列布局，左右固定，中间自适应。
<!--more-->

![w3school官网是三列固定布局][1]
----------


1.**浮动实现三列布局**
  这个类似两列布局的浮动，对左右div分别设置左右浮动，中间div设置margin-left和margin-right来实现，当然在html中的顺序应该是左右中。  
```
<html>
    <head>
        <title>margin负值实现三列布局</title>
    </head>
    <body>
        <div class="left">left</div>
        <div class="right">right</div>
        <div class="main">middle</div>
    </body>
</html>
```
```
body {
  width: 100%;
}
body .left {
  background: green;
  float: left;
  width: 100px;
}
body .right {
  background: yellow;
  float: right;
  width: 100px;
}
body .main {
  margin-left: 100px;
  margin-right: 100px;
  background: red;
}
body:after {
  content: "";
  display: table;
  clear: both;
  height: 0;
}
```

![](http://i1.buimg.com/567571/c8677b9bf71093b3.png)
----------


**2.margin负值实现三列布局**
原理同margin负值实现两列布局，不多说了。
```
<html>
  <head>
    <title>margin负值实现三列布局</title>
  </head>
  <body>
    <div class="main"> 
      <div class="content">middle</div>
    </div>
    <div class="left">left</div>
    <div class="right">right</div>
  </body>
</html>
```
```
body {
  width: 100%;
}
body .left {
  background: green;
  float: left;
  width: 100px;
  margin-left: -100%;
}
body .right {
  background: yellow;
  float: left;
  width: 100px;
  margin-left: -100px;
}
body .main {
  float: left;
  width: 100%;
  background: red;
}
body .main .content {
  margin: 0 100px;
}
body:after {
  content: "";
  display: table;
  clear: both;
  height: 0;
}
```
![](http://i1.buimg.com/567571/c8677b9bf71093b3.png)


----------
**3.flex实现三列布局**
和flex两列布局一个原理，对两边设置flex:0 0 100px,中间设置flex:auto。
```
<html>
  <head>
    <title>flex实现三列布局</title>
  </head>
  <body>
    <div class="left">left</div>
    <div class="main">middle</div>
    <div class="right">right</div>
  </body>
</html>
```
```
body {
  width: 100%;
  display: flex;
  display: -webkit-flex;
}
body .left {
  background: green;
  flex: 0 0 100px;
  height: 100px;
}
body .right {
  background: yellow;
  flex: 0 0 100px;
  height: 100px;
}
body .main {
  flex: auto;
  background: red;
  height: 100px;
}
```
![](http://i1.buimg.com/567571/c8677b9bf71093b3.png)

  [1]: https://segmentfault.com/img/bVzhEm