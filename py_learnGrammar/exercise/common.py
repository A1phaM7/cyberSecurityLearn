import csv
import re,pymysql
from pymysql.cursors import DictCursor


# 检查用户名
def check_username(username):
    if len(username) < 5 or len(username) > 12:
        return False

    if username[0] >= '0' and username[0] <= '9':
        return False

    for char in username:
        if not(ord(char) in range(65,91) or ord(char) in range(97,123) or ord(char) in range(48,58)):
            return False
    return True

# 检查密码
def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    lower = 0
    upper = 0
    digit = 0

    for char in password:
        if char >= 'A' and char <= 'Z':
            upper += 1
        elif char >= 'a' and char <= 'z':
            lower += 1
        elif char >= '0' and char <= '9':
            digit += 1

    if upper < 1 or lower < 1 or digit < 1:
        return False

    return True


# 修改密码
def change_password(username,newpass):
    csv_list = read_csv('./userpass.csv')
    for user in csv_list:
        if user['username'] == username:
            index = csv_list.index(user)
            break;
    csv_list[index]['password'] = newpass

    with open('./userpass.csv',mode = 'w') as f:
        f.write('username,password,phone\n')
        for user in csv_list:
            line = f"{user['username']},{user['password']},{user['phone']}\n"
            f.write(line)


# 检查手机号
def check_phone(phone):
    pattern = "^1[3-9]\d{9}$"
    if re.match(pattern,phone):
        return True
    else:
        return False

# 读取csv文件
def read_csv(csvfile,has_coloumn = True):
    with open('./userpass.csv') as f:
        line_list = f.readlines()

    if not has_coloumn:
        raise Exception('csv文件必须要使用第一行作为列名')
        # return None 
    key_list = line_list[0].strip().split(',')

    list = []
    for i in range(1,len(line_list)):
        temp_list = line_list[i].strip().split(',')

        dict = {}
        for j in range(len(key_list)):
            dict[key_list[j]] = temp_list[j]

        list.append(dict)
    return list     

result = read_csv('./userpass.csv',has_coloumn=True)


# 读取csv文件，并检查用户名是否存在
def check_user_exists(username):
    user_list = read_csv('./userpass.csv')
    for user in user_list:
        if(user['username']) == username:
            return True

    return False

# 读取csv文件，获取用户信息
def check_get_user(username):
    user_list = read_csv('./userpass.csv')
    for user in user_list:
        if(user['username']) == username:
            return user
    return None


# 针对数据库进行封装操作
def query_mysql(sql):
    try:
        conn = pymysql.connect(host='192.168.104.130', user='root', passwd='1997', database='learn', charset='utf8',
                           autocommit=True)
        cursor = conn.cursor(DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        raise Exception("数据库处理出错")
        conn.close()

# 数据库更新操作
# 针对数据库进行封装操作
def update_mysql(sql):
    conn = pymysql.connect(host='192.168.104.130', user='root', passwd='', database='learn', charset='utf8',
                       autocommit=True)
    cursor = conn.cursor(DictCursor)
    cursor.execute(sql) 
    conn.commit()
    conn.close()

    
# 全自动化测试
if __name__ == '__main__':
    pass
# def test_driver(func,expect,*args):
#     actual = func(*args)
#     if actual == expect:
#         print("测试 %s: 成功" % func.__name__)
#     else:
#         print("测试 %s: 失败" % func.__name__)

# test_driver(check_username,False,'132457')