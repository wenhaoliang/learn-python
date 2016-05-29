from django.db import models

# Create your models here.
from mongoengine import *

class ItemInfo(Document):

    title = StringField()
    url = StringField()
    pub_date = StringField()
    area = ListField(StringField())
    cates = ListField(StringField())
    look = StringField()
    time = StringField()
    price = IntField()
    meta = {'collection': 'item_info'}
