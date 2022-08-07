from exercise.common import *


def input_username():
    global username
    username = input("请输入用户名：")
    # 先检查用户名是否符合规则
    if check_username(username):
        if check_user_exists(username):
            print('用户名已被注册')
            input_username()
    elif check_username(username):
        print("用户名正确.")
    else:
        print("用户名错误.")
        input_username()


def input_password():
    global password
    password = input("请输入密码：")
    if check_password(password):
        print("密码正确.")
    else:
        print("密码错误.")
        input_password()


def input_phone():
    global phone
    phone = input("请输入手机号：")
    if check_phone(phone):
        print("手机号正确.")
    else:
        print("手机号错误.")
        input_phone()       

def do_change():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    user = check_get_user(username)
    if user is None:
        print('用户名不存在.')
        draw_menu()
    elif user['password'] == password:
        newpass = input('请输入您的新密码: ')
        change_password(username, newpass)
    else:
        print('旧密码验证不通过。')


def do_reg():
    input_username()
    if not check_user_exists(username):
        with open('./userpass.csv',mode='a') as f:
            f.write(f"\n{username},{password},{phone}")
            print('恭喜你注册成功！')
    input_password()
    input_phone()



    user_list = []
    user = {'username': username, 'password': password, 'phone': phone}
    user_list.append(user) 
    print(user_list)
    draw_menu()


def do_login():
    username = input("请输入用户名：") 
    password = input("请输入密码： ")
    user = check_get_user(username)
    if user is None:
        print('用户名不存在.')
        exit(0) 
    elif password == user[password]:
        print('登录成功') 
    else:
        print('登录失败')


def draw_menu():
    print('======== 欢迎使用用户管理系统 ========')
    print('1. 注册  2. 登录  3. 修改密码  4. 退出 ')
    option = input("请选择菜单选项：[1 2 3]: ")
    if option == '1':
        do_reg()
    elif option == '2':
        do_login()
    else:
        print('请输入正确的菜单编号.')
        draw_menu()


if __name__ == '__main__':
    # do_reg()    
    # do_login()
    do_change()
