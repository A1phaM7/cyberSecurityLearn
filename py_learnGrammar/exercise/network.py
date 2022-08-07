import socket


# # 建立与服务器连接
# s = socket.socket()
# s.connect(('192.168.104.131',554))
#
# content = 'welcome to CAUC 中国民航大学'
# s.send(content.encode())
#
# s.close()

# 定义一个服务器
def test_server():
    s = socket.socket()
    s.bind(('192.168.245.1', 555))
    s.listen()
    while True:
        chanel, client = s.accept()
        message = chanel.recv(1024)
        print(message.decode())


test_server()