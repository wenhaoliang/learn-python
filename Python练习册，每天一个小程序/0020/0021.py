# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0021 题： 请使用 Python 对密码加密
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)

    if isinstance(password, str):
        password = password.encode('UTF-8')

    ret = password
    for i in range(10):
        ret = HMAC(ret, salt, sha256).digest()

    return salt + ret