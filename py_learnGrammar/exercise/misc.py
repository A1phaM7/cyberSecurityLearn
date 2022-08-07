# import pymysql
# try:
#     conn = pymysql.connect(host='192.168.104.130', user='root', passwd='1997', database='learn', charset='utf8',
#                        autocommit=True)
#     cursor = conn.cursor()
#     cursor.execute('select * from users')
#     print('连接数据库成功')
# except pymysql.err.OperationalError as e:
#     print('数据库连接不正确')
# except pymysql.err.ProgrammingError as e:
#     print('sql语句不正确')
# finally:
#     conn.close()
#     print('无论怎样都会执行')

# # json的处理
# import json
# from exercise.common import query_mysql
#
#
# row_list = query_mysql('select username,password,role from user where userid < 6')
# print(row_list)
# print(type(row_list))
#
# jsonStr = json.dumps(row_list)
# print(jsonStr)
# print(type(jsonStr))

# 装饰器
import time
def stat(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return inner


@stat
def test02():
    result = 9999
    for i in range(3000):
        result = result + i - result * 15
    print(result)


test02()