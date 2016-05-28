from django.db import models

# Create your models here.
from mongoengine import *


# ORM

class ItemInfo(Document):
    title = StringField()
    url = StringField()
    pub_date = StringField()
    area = ListField(StringField())
    cates = ListField(StringField())
    look = StringField()
    time = StringField()
    price = IntField()
    meta = {'collection':'item_info'}

for i in ItemInfo.objects[:100]:
    print(i.price)