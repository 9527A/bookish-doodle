import requests
from bs4 import BeautifulSoup
import crawler_mongo
# import json

def download(i=1):
    novels = []

    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9'}
    
    r = requests.get('http://book.zongheng.com/store/c1/c0/b0/u0/p'+str(i)+'/v0/s9/t0/u0/i1/ALL.html', headers=h)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    
    items = soup.find_all('div', {'class': 'bookbox'})
    
    for num,item in enumerate(items):
        novel={}
        novel['id'] = num
        novel['name'] = item.find('div', {'class': 'bookname'}).text
        novel['src'] = item.find('div', {'class': 'bookimg'}).find('img')['src']
        novel['intro'] = item.find('div',{'class':'bookintro'}).text
        novels.append(novel)
        # print(novel['name'])
    
    crawler_mongo.data_seve(novels)
        
    return i
# download()