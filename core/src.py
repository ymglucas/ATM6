from interface import user_interface,bank_interface,shop_interface
from lib import common
user_info = {
    'name':None
}


def register():
    while True:
        name = input('请输入注册名(q退出)：')
        if name == 'q':
            break
        pwd = input('请输入注册密码：')
        re_pwd = input('请确认密码：')
        if pwd != re_pwd:
            print('密码不正确，请重新输入')
            continue
        flag,msg = user_interface.register_interface(name,pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)


def login():
    while True:
        name = input('请输入登入名(q退出)：')
        if name == 'q':
            break
        pwd = input('请输入密码：')
        flag,msg = user_interface.login_interface(name,pwd)
        if flag:
            user_info['name'] = name
            print(msg)
            break
        else:
            print(msg)


@common.auth
def check_balance():
    pass


def withdraw():
    pass


def transfer():
    pass


def repay():
    pass


def check_flow():
    pass


def shopping():
    pass


def check_shopping_cart():
    pass


def logout():
    pass


func_dic = {
    '1':register,
    '2':login,
    '3':check_balance,
    '4':withdraw,
    '5':transfer,
    '6':repay,
    '7':check_flow,
    '8':shopping,
    '9':check_shopping_cart,
    '0':logout
}


def run():
    while True:
        print('''
        1、注册
        2、登入
        3、查看余额
        4、提现
        5、转账
        6、还款
        7、查看流水
        8、购物
        9、查看购物车
        0、注销
        q、退出系统''')
        choice = input('请选择>>>:')
        if choice == 'q':
            break
        if choice in func_dic:
            func_dic[choice]()
        else:
            print('输入有误，请重新输入')


if __name__ == '__main__':
    print(123)
