from bs4 import BeautifulSoup
import requests

resp = requests.get('http://www.woniunote.com/')

# 初始化解析器
html = BeautifulSoup(resp.text, 'lxml')

print(html.head.title)
print(html.head.title.string)
print(html.div.div.div)

# find_all, select

# # 查找页面所有链接
links = html.find_all('a')
for link in links:
    print(link['href'])   
# 图片同理

# 根据id或class属性

# # 根据xpath风格进行查找 
titles = html.find_all('div', {'class':'title'})
for title in titles:
    print(title.string)

# 根据css选择器
titles = html.select('div.title')
for title in titles:
    print(title.string)




