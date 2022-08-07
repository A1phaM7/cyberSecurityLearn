import requests


# # 发送get请求
# resp = requests.get('https://liuhaiaacc.gitee.io/2022/03/14/linux-wang-luo-bian-cheng/')
# resp.encoding = 'utf-8'
# print(resp.text)

# post请求
data = {'username':'admin', 'password':'damin123', 'verifycode':'0000'}
resp = requests.post('https://localhost:8080/woniusales/user/login', data=data)
if resp.text == 'login-pass':
    print('登录成功')
else:
    print('登陆失败')

# # 下载图片
# resp = requests.get('http://www.woniunote.com/img/banner-1.jpg')
# with open('./banner.jpg', mode ='wb') as file:
#     file.write(resp.content)

# 登录成功后获取相应的cookie,用于在后续请求中使用
cookie = resp.cookies

# 文件上传
file = {'batchfile':open('E:/other/SaleList-20171020-Test.xls', 'rb')}
data = {'batchname':"GB20211009"}
resp = requests.post(url='http://localhost:8080/woniusales/goods/upload', data=data, files=file, cookies=cookie)
print(resp.text)
