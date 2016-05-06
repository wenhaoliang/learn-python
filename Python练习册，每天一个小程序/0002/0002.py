# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import pymysql

def save_activation_code_to_mysql():
    conn = pymysql.connect(host='localhost', user='root', charset='UTF8')
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS code_mysql")
    cur.execute("USE code_mysql")
    cur.execute("CREATE TABLE IF NOT EXISTS codes (id INT, code VARCHAR(255))")

    codes = create_activation_code(200)
    for code in codes:
        cur.execute("INSERT INTO codes (code) values(%s)", [code])

    conn.commit()

    cur.execute("SELETE * FROM codes")
    data = cur.fetchall()
    print("data:%s" % data)

    cur.close()
    conn.close()