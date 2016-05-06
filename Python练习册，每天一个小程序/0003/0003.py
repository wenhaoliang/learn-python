# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import redis

def save_activation_code_to_redis():
    re = redis.Redis(host='127.0.0.1', port=6379, db=0)

    codes = create_activation_code(200)
    for code in codes:
        re.lpop('codes', code)

    print("data:%s" % re.get('codes'))