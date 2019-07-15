from db import db_handler
from lib import common
logger = common.get('user')


def register_interface(name,pwd,balance=15000):
    user_dic = db_handler.select(name)
    if user_dic:
        return False,'用户名已存在'
    user_dic = {'name':name,'pwd':pwd,'balance':balance,'flow':[],'shopping_cart':{}}
    db_handler.save(user_dic)
    return True,'注册成功'


def login_interface(name,pwd):
    uesr_dic = db_handler.select(name)
    if not uesr_dic:
        return False,'用户名不存在'
    if pwd == uesr_dic['pwd']:
        logger.info('登入')
        return True,'登入成功'
    else:
        return False,'密码不正确'

