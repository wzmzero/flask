# MD5 的使用
import hashlib
import time

ctime =str(time.time())

def jm_md5(password):
    m = hashlib.sha1()  # 构建MD5对象
    m.update(password.encode(encoding='utf-8'))  # 设置编码格式 并将字符串添加到MD5对象中
    # m.update("123".encode("utf-8"))
    password_md5 = m.hexdigest()  # hexdigest()将加密字符串 生成十六进制数据字符串值
    return password, password_md5


g = jm_md5('789445456456456')
print(g)
print(ctime)
