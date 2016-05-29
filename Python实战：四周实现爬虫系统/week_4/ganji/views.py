from django.shortcuts import render
from django.core.paginator import Paginator
from ganji.models import ItemInfo
# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    limit = 3
    item_info = ItemInfo.objects
    paginatior = Paginator(item_info, limit)
    page = request.GET.get("page", 1)
    loaded = paginatior.page(page)
    print("-"*100)
    for i in loaded:
        print(i.price)

    context = {
        'ItemInfo': loaded,
    }

    return render(request, "pure_index_paginator.html", context)
