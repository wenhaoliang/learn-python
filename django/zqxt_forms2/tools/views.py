# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
from .forms import AddForm

def index(request):
    # 当提交表单时
    if request.method == 'POST':
        # form 包含提交的数据
        form = AddForm(request.POST)
        # 如果提交的数据合法
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']

            return HttpResponse(str(int(a) + int(b)))

    else:
        form = AddForm()

    return render(request, 'index.html', {'form': form})