import requests
from bs4 import BeautifulSoup
# import json

def download():#这里可以传入爬取第几页.待完成
    novels = []

    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9'}
    
    r = requests.get('http://book.zongheng.com/store/c1/c0/b0/u0/p1/v0/s9/t0/u0/i1/ALL.html', headers=h)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    
    items = soup.find_all('div', {'class': 'bookbox'})
    
    for item in items:
        novel={}
        novel['name'] = item.find('div', {'class': 'bookname'}).text
        novel['intro'] = item.find('div', {'class': 'bookintro'}).text
        novel['src'] = item.find('div', {'class': 'bookimg'}).find('img')['src']
        novels.append(novel)
        # print(novel['name'])
        
    return novels
    #这里调用数据库导入函数.待完成
# download()