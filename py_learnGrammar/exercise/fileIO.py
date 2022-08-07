# coding=utf-8
# from cgi import test
#
# f = open('./test.TXT')
# content = f.read()
# print(content)
# f.close()
#
# # 写
# f = open('./test.txt',mode = 'a')
# f.write("\nSecond line")
# f.close()

# csv文件
f = open('./userpass.csv','r',encoding='utf-8')
line_list = f.readlines()

user_list = []
#username,password,expect
for i in range(1,len(line_list)):
    line = line_list[i].strip()
    print(line)

    username = line.split(',')[0]
    password = line.split(',')[1]
    expect = line.split(',')[2]

    user_dict = {}
    user_dict['username'] = username
    user_dict['password'] = password
    user_dict['expect'] = expect

    user_list.append(user_dict)

