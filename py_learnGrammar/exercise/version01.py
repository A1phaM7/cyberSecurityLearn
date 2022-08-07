from exercise.common import check_username,check_password,check_phone

def input_username():
    global username
    username = input("请输入用户名：")
    if check_username(username):
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

def do_reg():
    input_username()
    input_password()
    input_phone()

    user_list = []
    user = {'username':username,'password':password,'phone':phone}
    user_list.append(user) 
    print(user_list) 

if __name__ == '__main__':
    do_reg()    