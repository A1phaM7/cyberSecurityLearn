import pymysql

# # 建立连接
# conn = pymysql.connect(host='192.168.104.130', user='root', passwd='', database='learn', charset='utf8')
# print(conn.host_info)

# # 操作数据库
# cursor = conn.cursor()

# sql = "select username,password,role from user where userid < 3"
# cursor.execute(sql)

# result = cursor.fetchall()
# print(result)

# conn.close()

# 字典

# 更新操作
# 必须确认提交，两种方式
conn = pymysql.connect(host='192.168.104.130', user='root', passwd='1997', database='learn', charset='utf8',
                       autocommit=True)
print(conn.host_info)
cursor = conn.cursor()
sql = "update user set password='12345678' where userid = 3"
cursor.execute(sql)
# conn.commit()
conn.close()
