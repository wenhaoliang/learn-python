
---
title: 'CSS中那些布局(两栏布局)  '
date: 2016-08-23 14:24:49
tags: 前端 html css
---



**最近在做IFE的前端任务，在前五个任务中分别使用了两栏布局和三栏布局，现在来整理一下。**
-----------------------------------------------


两列自适应布局算是css布局里面最基础的一种布局了，不少网站在使用。
这种布局通常是左侧固定，右边自适应，当然也有反过来的，道理一样，这里有好几种方法。
<!--more-->
![张鑫旭老师的博客是左边流式布局自适应，右边固定宽度][1]


----------


**1.左浮动+margin**
 因为浮动会导致元素脱离文档流，所以下面的元素会占据浮动元素原来的位置。
 这个时候只要对右边元素设置margin-left:左边div宽度 就可以实现自适应布局。
```
<html>
    <head>
        <title>左浮动+margin</title>
    </head>
    <body>
        <div class="left">left</div>
        <div class="right">right</div>
    </body>
</html>
```

```
body{  
    width:100%;  
    position:relative;  
 }
.left{    
    float:left;    
    width:100px;    
    background:green;  
 }  
.right{    
    background:yellow;    
    margin-left:100px; 
 }
```
![](http://i1.buimg.com/567571/e40a1d7fb7564d27.png)

--------
**2.绝对定位实现两列布局**
这个原理类似浮动，因为绝对定位会脱离文档流，只需要设置右div的margin-left就能实现布局。

```
 <html>
    <head>
        <title>绝对定位实现两列布局</title>
    </head>
    <body>
        <div class="left">left</div>
        <div class="right">right</div>
    </body>
</html>
```
 
```
 body{  
    width:100%;  
    position:relative;  
 }
 .left{    
    position:absolute;    
    width:100px;    
    background:green;  
 }  
 .right{    
    background:yellow;    
    margin-left:100px; 
 }
```
![](http://i1.buimg.com/567571/e40a1d7fb7564d27.png)

----------


**3.flex实现两列布局**
flex布局一直挺好用，无奈兼容性捉急，ie10+才支持。 
注意，设为Flex布局以后，子元素的float、clear和vertical-align属性将失效。  
flex布局默认项目是主轴为水平方向，最主要的是flex属性。flex属性是flex-grow, flex-shrink 和 flex-basis的简写，默认值为0 1 auto。  
大概就是给左边的div一个固定值，然后给右边设置flex:auto;来实现两列布局。  
这里不多对flex布局介绍，有兴趣的可以看一下阮一峰老师的这篇博客:
[Flex 布局教程：语法篇][2]
```
<html>
    <head>
        <title>flex实现两列布局</title>
    </head>
    <body>
        <div class="left">left</div>
        <div class="right">right</div>
    </body>
</html>

```
```
body{
    width:100%;
    display:flex;
    display:-webkit-flex;
}
.left{
    flex:0 0 100px;
    background:green;
    height:100px;
}
.right{
    flex:auto;
    height:100px;
    background:yellow;
}

```
![](http://i1.buimg.com/567571/96d68dccff749643.png)

----------


**4.calc实现两列布局**
这是css3里面的新属性，兼容性还可以，在ie9+、FF4.0+、Chrome19+、Safari6+都得到了支持。  
 
通过calc可以使用百分比、em、px和rem单位值计算出其宽度或者高度，这样就不用考虑div值到底是多少。所以可以对右边div设置width:calc(100%-100px);来实现自适应布局。  
 
```
 <html>
    <head>
    <title>calc实现两列布局</title>
     </head>
    <body>
    <div class="left">left</div>
    <div class="right">right</div>
    </body>
</html>

```
```
body{
    width:100%;
}
.left{
    width:100px;
    background:green;
    float: left;
}
.right{
    width:calc(100% - 100px);
    width:-moz-calc(100% - 100px);
    width:-webkit-calc(100% - 100px);
    background:yellow;
    float: left;
}
&:after{
    content:"";
    display:table;
    clear:both;
    height:0;
}
```
![](http://i1.buimg.com/567571/e40a1d7fb7564d27.png)

----------
**5.浮动+margin负值来实现**

实现方法是给右边的div外面再套上一个父div，然后让父div的宽度设为100%。
对父div和左边的div都设置左浮动，再让左div的margin-left:-100%,右div设置margin-left:左div的宽度。
这样就实现了自适应布局，当然左右div的前后顺序要反过来。
 
```
<html>
	<head>
    <title>浮动+margin负值来实现</title>
    </head>
    <body>
		<div class="main">
			<div class="right">right</div>	
		</div>  
    <div class="left">left</div>
    </body>
</html>

```
```
body{
  width:100%;
}
  .main{
    float: left;
    width:100%;
}
.right{
      margin-left:100px;
      background-color:yellow;
}


  .left{
    width: 100px;
    float: left;
    margin-left: -100%;
    background-color: green;
}



```
![](http://i1.buimg.com/567571/e40a1d7fb7564d27.png)

----------




  [1]: https://segmentfault.com/img/bVzhEk
  [2]: http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html?utm_source=tuicool