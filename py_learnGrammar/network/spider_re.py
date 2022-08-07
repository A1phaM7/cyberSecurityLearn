import re
import time

import requests
def download_page():
    resp = requests.get('http://www.woniunote.com/')

    links = re.findall('<a href="(.+?)"', resp.text)
    for link in links:
        if 'articleid' in link or link.startswith('#'):
            continue
        if link.startswith('/'):
            link = 'http://www.woniunote.com/' + link
        print(link)
        #  将页面文件保存于本地
        resp = requests.get(link)
        resp.encoding = 'utf-8'
        filename = link.split('/')[-1] + time.strftime("_%Y%m%d_%H%M%S") + '.html'
        with open(f"./woniunote/page/{filename}", mode='w', encoding='utf-8') as file:
            file.write(resp.text)

