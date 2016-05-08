#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
 
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
	
def home(request):
    return render(request, "home.html")
	
def home(request):
    string = u'我在自强学堂学习Django，用它来建网站'
    return render(request, 'home.html', {'string': string})

def home(request):
    TutorialList = ['HTML', 'CSS', 'jQuery', 'Python', 'Django']
    return render(request, 'home.html', {'TutorialList': TutorialList})
	
def home(request):
	info_dict = {'site': u"大懒虫", 'content':u"奇妙的世界"}
	return render(request, "home.html", {'info_dict': info_dict})

def home(request):
	List = map(str, range(1000)) 
	return render(request, 'home.html', {'List': List})