import threading, time

# 单线程情况下，5s
def test_01():
    print(threading.current_thread().getName())
    for i in range(5):
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)


# 使用多线程的方式输入5次时间
def test_02():
    print(threading.current_thread().getName())
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)


# 使用多线程模拟流量泛洪


if __name__ == '__main__':
    # test_01()
    for i in range(5):
        t = threading.Thread(target=test_02)
        t.start()