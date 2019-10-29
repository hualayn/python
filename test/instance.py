from flask import g #导入全局对象

def log_a():
    print('log a %s' % g.username) #引用全局对象g.username(这个参数已经在g.py中赋值)

def log_b():
    print('log b %s' % g.username)

def log_c():
    print('log c %s' % g.username)